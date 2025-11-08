"""
Signal handlers for the blog app.

This module contains signal handlers that respond to model events,
particularly for post publication notifications.
"""
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Post)
def post_published_handler(sender, instance, created, **kwargs):
    """
    Signal handler triggered when a post is saved.
    
    Detects when a post status changes to 'published' and logs the publication event.
    This handler includes error handling to ensure signal failures don't block post saves.
    
    Args:
        sender: The model class (Post)
        instance: The actual Post instance being saved
        created: Boolean indicating if this is a new record
        **kwargs: Additional keyword arguments from the signal
    
    Requirements: 15.1, 15.2, 15.3, 15.4, 15.5
    """
    try:
        # Only process if the post is being updated (not created) and status is published
        if not created and instance.status == 'published':
            logger.info(
                f'Post published: "{instance.title}" by {instance.author.username} '
                f'(ID: {instance.id}, Slug: {instance.slug})'
            )
            # Future enhancements can be added here:
            # - Send email notifications to subscribers
            # - Update RSS feed
            # - Trigger social media posts
            # - Update search index
            
    except Exception as e:
        # Log the error but don't raise it to prevent blocking the post save
        logger.error(
            f'Error in post_published_handler for post ID {instance.id}: {str(e)}',
            exc_info=True
        )
