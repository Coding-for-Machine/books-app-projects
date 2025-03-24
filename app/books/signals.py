from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Download, Like

@receiver(post_save, sender=Like)
@receiver(post_delete, sender=Like)
def update_likes_count(sender, instance, **kwargs):
    instance.book.likes_count = instance.book.likes.count()
    instance.book.save()

@receiver(post_save, sender=Download)
@receiver(post_delete, sender=Download)
def update_downloads_count(sender, instance, **kwargs):
    instance.book.downloads_count = instance.book.downloads.count()
    instance.book.save()
