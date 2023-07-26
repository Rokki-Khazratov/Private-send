from django.contrib import admin
from .models import Message,Content

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['get_text_preview','id','is_read']
    list_filter = ['is_read']

    def get_text_preview(self, obj):
        words = obj.text.split()[:10]
        preview = ' '.join(words)
        return preview + '...' if len(obj.text.split()) > 5 else preview

    get_text_preview.short_description = 'text Preview'

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['title','id']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
