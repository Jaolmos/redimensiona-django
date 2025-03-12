from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    """Manager personalizado para el modelo de Usuario."""
    
    def create_user(self, email, password=None, **extra_fields):
        """Crear y guardar un usuario con el email y contraseña dados."""
        if not email:
            raise ValueError(_('El Email es obligatorio'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """Crear y guardar un superusuario con el email y contraseña dados."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('El superusuario debe tener is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('El superusuario debe tener is_superuser=True.'))
        
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    """Modelo de usuario personalizado que usa email como identificador único."""
    
    username = None  # Deshabilitamos el campo username
    email = models.EmailField(_('dirección de correo'), unique=True)
    
    # Campos adicionales
    bio = models.TextField(_('biografía'), blank=True)
    
    # Definimos campo de inicio de sesión y campos requeridos
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    # Asignamos el manager personalizado
    objects = UserManager()
    
    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')
    
    def __str__(self):
        return self.email