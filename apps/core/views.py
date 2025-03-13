from django.shortcuts import render

def home(request):
    """Vista para la página principal."""
    return render(request, 'core/home.html')