@description('Azure region to deploy resources into')
param location string = resourceGroup().location

@description('Name for the web app')
param appName string = toLower(replace('blogbreeze-${uniqueString(resourceGroup().id)}','_','-'))

@description('Python major.minor version for App Service on Linux')
param pythonVersion string = '3.11'

@description('Django SECRET_KEY for the application')
@secure()
param secretKey string

@description('PostgreSQL Flexible Server admin username')
param postgresAdminUser string = 'pgadmin'

@description('PostgreSQL Flexible Server admin password')
@secure()
param postgresAdminPassword string

@description('PostgreSQL version')
param postgresVersion string = '16'

@description('Database name for the app')
param dbName string = 'blogbreeze'

@description('Name for the storage account used for media files')
param storageAccountName string = toLower('st${uniqueString(resourceGroup().id)}')

// Application Insights (optional but recommended)
resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: '${appName}-ai'
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
  }
}

// App Service Plan (Linux)
resource appServicePlan 'Microsoft.Web/serverfarms@2023-12-01' = {
  name: '${appName}-plan'
  location: location
  sku: {
    name: 'B1'
    tier: 'Basic'
    size: 'B1'
    capacity: 1
  }
  kind: 'linux'
  properties: {
    reserved: true
  }
}

// Storage Account for media
resource storage 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false
    supportsHttpsTrafficOnly: true
  }
}

resource blobService 'Microsoft.Storage/storageAccounts/blobServices@2023-01-01' = {
  name: 'default'
  parent: storage
  properties: {}
}

@description('Container to store user-uploaded media')
param mediaContainerName string = 'media'

resource mediaContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-01-01' = {
  name: mediaContainerName
  parent: blobService
  properties: {
    publicAccess: 'None'
  }
}

// PostgreSQL Flexible Server
resource pgServer 'Microsoft.DBforPostgreSQL/flexibleServers@2023-06-01' = {
  name: '${appName}-pg'
  location: location
  sku: {
    name: 'Standard_B1ms'
    tier: 'Burstable'
  }
  properties: {
    version: postgresVersion
    administratorLogin: postgresAdminUser
    administratorLoginPassword: postgresAdminPassword
    storage: {
      storageSizeGB: 32
    }
    backup: {
      backupRetentionDays: 7
      geoRedundantBackup: 'Disabled'
    }
    highAvailability: {
      mode: 'Disabled'
    }
    network: {
      publicNetworkAccess: 'Enabled'
    }
  }
}

resource pgDb 'Microsoft.DBforPostgreSQL/flexibleServers/databases@2023-06-01' = {
  name: dbName
  parent: pgServer
  properties: {}
}

// Dev-friendly firewall rule (allow all). Replace with tighter rules for production.
resource pgFirewallAllowAll 'Microsoft.DBforPostgreSQL/flexibleServers/firewallRules@2023-06-01' = {
  name: 'AllowAll'
  parent: pgServer
  properties: {
    startIpAddress: '0.0.0.0'
    endIpAddress: '255.255.255.255'
  }
}

// Web App (Linux)
resource webApp 'Microsoft.Web/sites@2023-12-01' = {
  name: appName
  location: location
  kind: 'app,linux'
  properties: {
    serverFarmId: appServicePlan.id
    httpsOnly: true
    siteConfig: {
      linuxFxVersion: 'PYTHON|${pythonVersion}'
      appCommandLine: 'gunicorn BlogBreeze.wsgi:application'
      alwaysOn: true
    }
  }
}

// App settings
var databaseUrl = 'postgresql://${postgresAdminUser}:${postgresAdminPassword}@${pgServer.name}.postgres.database.azure.com:5432/${dbName}?sslmode=require'
resource webAppSettings 'Microsoft.Web/sites/config@2023-12-01' = {
  name: 'appsettings'
  parent: webApp
  properties: {
    SCM_DO_BUILD_DURING_DEPLOYMENT: 'true'
    WEBSITES_ENABLE_APP_SERVICE_STORAGE: 'true'
    PYTHON_VERSION: pythonVersion
    SECRET_KEY: secretKey
    DATABASE_URL: databaseUrl
    AZURE_ACCOUNT_NAME: storage.name
    AZURE_CONTAINER: mediaContainerName
    // NOTE: For production, prefer a managed identity + SAS instead of exposing account key.
    AZURE_ACCOUNT_KEY: storage.listKeys().keys[0].value
  }
}

output webAppName string = webApp.name
output webUrl string = 'https://${webApp.name}.azurewebsites.net'
output storageAccountName string = storage.name
output storageContainer string = mediaContainerName
output postgresHost string = '${pgServer.name}.postgres.database.azure.com'
output databaseName string = dbName
