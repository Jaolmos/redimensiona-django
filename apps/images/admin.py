from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Image, Thumbnail

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """Admin para el modelo Image."""
    list_display = ('id', 'title', 'user', 'uploaded_at', 'get_thumbnails_count')
    list_filter = ('uploaded_at', 'user')
    search_fields = ('title', 'user__email')
    readonly_fields = ('uploaded_at',)
    
    def get_thumbnails_count(self, obj):
        return obj.thumbnails.count()
    get_thumbnails_count.short_description = _('Miniaturas')

@admin.register(Thumbnail)
class ThumbnailAdmin(admin.ModelAdmin):
    """Admin para el modelo Thumbnail."""
    list_display = ('id', 'image', 'width', 'height', 'created_at')
    list_filter = ('created_at', 'width', 'height')
    search_fields = ('image__title',)
    readonly_fields = ('created_at',)
