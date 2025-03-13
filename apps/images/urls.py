from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('upload/', views.upload_image, name='upload'),
    path('results/<int:image_id>/', views.image_results, name='results'),
]