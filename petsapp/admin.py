from django.contrib import admin
from .models import Media

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'media_type', 'format', 'size_mb', 'duration_secs')
    list_filter = ('media_type',)
