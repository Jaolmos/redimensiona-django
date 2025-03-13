import os 
from celery import Celery

# Establecer la variable de entorno para las configuraciones de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('redimensiona')

# Configuración de Celery con Django (namespace='CELERY_' para settings)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Buscar tareas automáticamente en todas las aplicaciones registradas
app.autodiscover_tasks()

# Tarea de depuración para verificar que Celery está funcionando
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
