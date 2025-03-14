from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Image

class ImageUploadForm(forms.ModelForm):
    """Formulario para subir imágenes."""
    
    # Tamaños predefinidos
    size_sm = forms.BooleanField(
        label=_('Pequeño (300x300px)'),
        required=False,
        initial=True
    )
    size_md = forms.BooleanField(
        label=_('Mediano (600x600px)'),
        required=False,
        initial=True
    )
    size_lg = forms.BooleanField(
        label=_('Grande (1200x1200px)'),
        required=False,
        initial=True
    )
    
    # Tamaño personalizado
    custom_height = forms.IntegerField(
        label=_('Alto personalizado'),
        required=False,
        min_value=10,
        max_value=2000,
        help_text=_('Deja en blanco para calcular automáticamente basado en el ancho')
    )
    
    custom_width = forms.IntegerField(
        label=_('Ancho personalizado'),
        required=False,
        min_value=10,
        max_value=2000,
        help_text=_('Deja en blanco para calcular automáticamente basado en el alto')
    )
    
    
    class Meta:
        model = Image
        fields = ['original_image', 'title']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': _('Título (opcional)')}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        custom_width = cleaned_data.get('custom_width')
        custom_height = cleaned_data.get('custom_height')
        
        # Si se especificó un tamaño personalizado, al menos uno de los valores debe estar presente
        if (custom_width or custom_height) and not (custom_width and custom_height):
            # Esto está bien, el usuario especificó solo uno de los valores
            pass
        elif custom_width and custom_height:
            # El usuario especificó ambos valores, esto también está bien
            pass
        
        return cleaned_data
    
    def clean_original_image(self):
        image = self.cleaned_data.get('original_image')
        user = self.initial.get('user', None)
        
        # Límite para usuarios anónimos: 5MB
        # Límite para usuarios registrados: 20MB
        max_size_anonymous = 5 * 1024 * 1024  # 5MB en bytes
        max_size_registered = 20 * 1024 * 1024  # 20MB en bytes
        
        if image:
            if not user and image.size > max_size_anonymous:
                raise forms.ValidationError(
                    _("El tamaño máximo permitido para usuarios anónimos es de 5MB. Por favor, regístrate para subir archivos más grandes.")
                )
            elif user and image.size > max_size_registered:
                raise forms.ValidationError(
                    _("El tamaño máximo permitido es de 20MB.")
                )
        
        return image