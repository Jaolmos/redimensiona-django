import os
import uuid
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

def image_upload_path(instance, filename):
    """Genera una ruta única para cada imagen subida."""
    ext = filename.split('.')[-1]
    new_filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('uploads', 'images', new_filename)

class Image(models.Model):
    """Modelo para almacenar imágenes y sus miniaturas."""
    
    title = models.CharField(_('título'), max_length=255, blank=True)
    original_image = models.ImageField(_('imagen original'), upload_to=image_upload_path)
    uploaded_at = models.DateTimeField(_('fecha de subida'), auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='images',
        null=True,
        blank=True,
        verbose_name=_('usuario')
    )
    
    # Campo para almacenar la sesión de usuarios anónimos
    session_key = models.CharField(_('clave de sesión'), max_length=40, null=True, blank=True)
    
    def __str__(self):
        return self.title or f"Imagen {self.id}"
    
    class Meta:
        verbose_name = _('imagen')
        verbose_name_plural = _('imágenes')
        ordering = ['-uploaded_at']

class Thumbnail(models.Model):
    """Modelo para almacenar las miniaturas de las imágenes."""
    
    image = models.ForeignKey(
        Image, 
        on_delete=models.CASCADE, 
        related_name='thumbnails',
        verbose_name=_('imagen original')
    )
    file = models.ImageField(_('archivo'), upload_to='uploads/thumbnails/')
    width = models.PositiveIntegerField(_('ancho'))
    height = models.PositiveIntegerField(_('alto'))
    created_at = models.DateTimeField(_('fecha de creación'), auto_now_add=True)
    
    def __str__(self):
        return f"Miniatura {self.width}x{self.height} de {self.image}"
    
    class Meta:
        verbose_name = _('miniatura')
        verbose_name_plural = _('miniaturas')
        ordering = ['width', 'height']