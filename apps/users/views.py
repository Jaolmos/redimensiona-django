from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from apps.images.models import Image
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .forms import UserRegistrationForm

def register(request):
    """Vista para registrar un nuevo usuario."""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Autenticamos y logueamos al usuario automáticamente
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, _("¡Registro exitoso! Bienvenido/a a Redimensiona."))
            return redirect('core:home')  # Redirigir a la página de inicio
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    """Vista personalizada para cerrar sesión"""
    logout(request)
    return redirect('core:home')


@login_required
def dashboard(request):
    """Vista del panel de control del usuario."""
    # Obtener todas las imágenes del usuario
    user_images = Image.objects.filter(user=request.user).order_by('-uploaded_at')
    
    return render(request, 'users/dashboard.html', {
        'user_images': user_images
    })


@login_required
def delete_image(request, image_id):
    """Vista para eliminar una imagen del usuario."""
    image = get_object_or_404(Image, id=image_id, user=request.user)
    
    # Eliminar la imagen y todas sus miniaturas
    image.delete()
    
    messages.success(request, _("La imagen ha sido eliminada correctamente."))
    return redirect('users:dashboard')