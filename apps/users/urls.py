from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete-image/<int:image_id>/', views.delete_image, name='delete_image'),
    ]