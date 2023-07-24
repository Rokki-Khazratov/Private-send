from django.db import models

class Message(models.Model):
    text = models.TextField(max_length=4000)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)