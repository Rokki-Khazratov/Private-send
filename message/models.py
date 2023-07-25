from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Message(models.Model):
    text = models.TextField(max_length=4000)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def mark_as_read(self):
        self.is_read = True
        self.save()

    def delete_after_read(self):
        if self.is_read:
            self.delete()

@receiver(post_save, sender=Message)
def auto_delete_message(sender, instance, **kwargs):
    if instance.is_read:
        instance.delete()
