import os
from io import BytesIO
from PIL import Image as PILImage
from django.core.files.base import ContentFile

def resize_image(image_content, width=None, height=None):
    """
    Redimensiona una imagen manteniendo su proporción.
    
    Args:
        image_content: Contenido binario de la imagen
        width: Ancho deseado (opcional)
        height: Alto deseado (opcional)
    
    Returns:
        ContentFile: Objeto de archivo con la imagen redimensionada
        tuple: (width_real, height_real) con las dimensiones finales
    """
    from io import BytesIO
    from PIL import Image as PILImage
    from django.core.files.base import ContentFile
    
    # Crear objeto de imagen desde el contenido binario
    img_io = BytesIO(image_content)
    img = PILImage.open(img_io)
    
    # Convertir a RGB si es necesario
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    original_width, original_height = img.size
    aspect_ratio = original_width / original_height
    
    # Determinar las dimensiones finales
    if width and height:
        # Ambas dimensiones especificadas, usar thumbnail para mantener proporción
        new_width, new_height = width, height
    elif width:
        # Solo ancho especificado, calcular alto manteniendo proporción
        new_width = width
        new_height = int(width / aspect_ratio)
    elif height:
        # Solo alto especificado, calcular ancho manteniendo proporción
        new_height = height
        new_width = int(height * aspect_ratio)
    else:
        # Si no se especificó ninguna dimensión, usar el tamaño original
        return ContentFile(image_content), (original_width, original_height)
    
    # Redimensionar la imagen
    img = img.resize((new_width, new_height), PILImage.LANCZOS)
    
    # Guardar la imagen redimensionada en un buffer
    output = BytesIO()
    img.save(output, format='JPEG', quality=85)
    output.seek(0)
    
    return ContentFile(output.getvalue()), (new_width, new_height)