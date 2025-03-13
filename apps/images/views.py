import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .models import Image, Thumbnail
from .forms import ImageUploadForm
from .utils import resize_image
from .tasks import process_image_thumbnails


def upload_image(request):
    """Vista para subir y procesar imágenes."""

    # Verificar límites para usuarios anónimos
    if not request.user.is_authenticated:
        # Obtener clave de sesión
        if not request.session.session_key:
            request.session.save()

        # Contar imágenes procesadas en esta sesión
        session_images_count = Image.objects.filter(
            session_key=request.session.session_key
        ).count()

        # Limitar a 3 imágenes por sesión para usuarios anónimos
        if session_images_count >= 3:
            messages.warning(
                request,
                _("Has alcanzado el límite de 3 imágenes como usuario anónimo. Por favor, regístrate para procesar más imágenes.")
            )
            return redirect('users:register')

    if request.method == 'POST':
        # Pasar el usuario al formulario para verificar límites
        form = ImageUploadForm(
            request.POST,
            request.FILES,
            initial={
                'user': request.user if request.user.is_authenticated else None}
        )
        if form.is_valid():
            # Guardar la imagen sin procesar
            image = form.save(commit=False)

            # Asignar usuario o clave de sesión
            if request.user.is_authenticated:
                image.user = request.user
            else:
                # Guardar la clave de sesión para usuarios anónimos
                image.session_key = request.session.session_key
                if not image.session_key:
                    request.session.save()
                    image.session_key = request.session.session_key

            image.save()

            # Procesar las miniaturas seleccionadas
            sizes = []
            if form.cleaned_data['size_sm']:
                sizes.append((300, None))
            if form.cleaned_data['size_md']:
                sizes.append((600, None))
            if form.cleaned_data['size_lg']:
                sizes.append((1200, None))

            # Añadir tamaño personalizado si se especificó
            custom_width = form.cleaned_data['custom_width']
            custom_height = form.cleaned_data['custom_height']
            if custom_width or custom_height:
                sizes.append((custom_width, custom_height))

            # Iniciar tarea asíncrona para procesar las miniaturas
            process_image_thumbnails.delay(image.id, sizes)

            messages.success(request, _(
                "Imagen subida correctamente. Las miniaturas se están procesando y estarán disponibles en breve."))
            return redirect('images:results', image_id=image.id)
    else:
        # Pasar el usuario al formulario también en GET
        form = ImageUploadForm(
            initial={
                'user': request.user if request.user.is_authenticated else None}
        )

    return render(request, 'images/upload_form.html', {'form': form})


def image_results(request, image_id):
    """Vista para mostrar los resultados del procesamiento."""
    image = get_object_or_404(Image, id=image_id)

    # Verificar que el usuario tenga permiso para ver esta imagen
    if request.user.is_authenticated:
        if image.user and image.user != request.user:
            messages.error(request, _(
                "No tienes permiso para ver estos resultados."))
            return redirect('core:home')
    elif image.session_key != request.session.session_key:
        messages.error(request, _(
            "No tienes permiso para ver estos resultados."))
        return redirect('core:home')

    # Verificar si hay miniaturas
    has_thumbnails = image.thumbnails.exists()

    return render(request, 'images/results.html', {
        'image': image,
        'has_thumbnails': has_thumbnails
    })
