from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
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