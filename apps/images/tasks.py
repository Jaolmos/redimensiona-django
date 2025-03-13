from celery import shared_task
import os
from .models import Image, Thumbnail
from .utils import resize_image

@shared_task
def process_image_thumbnails(image_id, sizes):
    """
    Tarea para procesar miniaturas de una imagen de forma asíncrona.
    """
    try:
        # Obtener la imagen
        image = Image.objects.get(id=image_id)
        
        # Generar las miniaturas
        for width, height in sizes:
            # Generar nombre para la miniatura
            original_name = os.path.basename(image.original_image.name)
            name_parts = original_name.rsplit('.', 1)
            if len(name_parts) > 1:
                base_name = name_parts[0]
                ext = name_parts[1]
            else:
                base_name = original_name
                ext = 'jpg'
            
            # Nombrar según los parámetros proporcionados
            if width and height:
                thumbnail_name = f"{base_name}_{width}x{height}.jpg"
            elif width:
                thumbnail_name = f"{base_name}_w{width}.jpg"
            elif height:
                thumbnail_name = f"{base_name}_h{height}.jpg"
            
            # Redimensionar la imagen - Modificación para Windows
            # Abrir el archivo de manera segura
            with image.original_image.open('rb') as img_file:
                # Leer todo el contenido del archivo
                img_content = img_file.read()
                # Pasar el contenido a la función resize_image
                thumbnail_content, (real_width, real_height) = resize_image(img_content, width, height)
            
            # Crear y guardar la miniatura con dimensiones reales
            thumbnail = Thumbnail(image=image, width=real_width, height=real_height)
            thumbnail.file.save(thumbnail_name, thumbnail_content, save=True)
        
        return f"Procesadas {len(sizes)} miniaturas para la imagen {image_id}"
    
    except Exception as e:
        return f"Error procesando miniaturas: {str(e)}"