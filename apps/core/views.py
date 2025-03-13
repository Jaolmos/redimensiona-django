from django.shortcuts import render
from apps.images.forms import ImageUploadForm

def home(request):
    """Vista para la página principal."""
    form = ImageUploadForm()
    return render(request, 'core/home.html', {'form': form})