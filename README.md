# Redimensiona 🖼️

Redimensiona es una aplicación web desarrollada con Django que permite a los usuarios redimensionar imágenes de forma inteligente, manteniendo la calidad y las proporciones originales. Ideal para optimizar imágenes para web, redes sociales o cualquier uso específico.

## ✨ Características Principales

- **Procesamiento Inteligente**
  - Redimensionamiento manteniendo proporciones
  - Vista previa en tiempo real
  - Cálculo automático de dimensiones
  - Procesamiento asíncrono
  - Múltiples formatos soportados

- **Planes Gratuitos**
  - Plan sin registro:
    • 3 imágenes gratuitas
    • Hasta 2MB por imagen
    • Proceso instantáneo
    • Sin necesidad de cuenta
  - Plan con registro:
    • Imágenes ilimitadas
    • Hasta 20MB por imagen
    • Acceso permanente
    • Historial de imágenes

## 🛠️ Tecnologías

### Backend
- Django 5.0
- Celery (procesamiento asíncrono)
- Redis (message broker)
- MySQL
- Pillow (procesamiento de imágenes)

### Frontend
- HTML5
- CSS3 (diseño personalizado)
- JavaScript vanilla
- Diseño responsive
- Animaciones y transiciones

### Características Técnicas
- Procesamiento asíncrono con Celery
- Sistema de colas con Redis
- Base de datos MySQL
- Almacenamiento optimizado de imágenes

## 📂 Estructura del Proyecto

```
redimensiona/
├── apps/
│   ├── core/          # Funcionalidad principal
│   ├── images/        # Procesamiento de imágenes
│   └── users/         # Gestión de usuarios
├── config/            # Configuración del proyecto
├── static/
│   ├── css/          # Estilos
│   └── js/           # Scripts
│       ├── preview.js    # Vista previa de imágenes
│       └── lightbox.js   # Visualización de imágenes
├── templates/         # Plantillas HTML
├── media/            # Archivos subidos
└── requirements.txt   # Dependencias
```

## ⚙️ Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tuusuario/redimensiona.git
cd redimensiona
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar variables de entorno
```bash
cp .env.example .env
```
Editar `.env` con tus configuraciones:
```
# Configuración de Django
DEBUG=True
SECRET_KEY=tu_clave_secreta

# Configuración de la base de datos
DB_NAME=redimensiona_db
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña

# Configuración de Redis y Celery
REDIS_USERNAME=tu_usuario_redis
REDIS_PASSWORD=tu_contraseña_redis
```

### 4. Configurar la base de datos
```bash
python manage.py migrate
```

### 5. Iniciar servicios
```bash
# Terminal 1: Django
python manage.py runserver

# Terminal 2: Celery
# En Linux/Mac:
celery -A redimensiona worker -l info

# En Windows:
celery -A config worker --pool=solo -l INFO
```

## 🚀 Planes Futuros

- Más opciones de procesamiento
- Filtros y efectos
- API REST
- Integración con servicios cloud
- Sistema de pagos para planes premium

## 🎨 Características de Diseño

- Interfaz moderna y minimalista
- Tema claro con acentos de color
- Animaciones suaves
- Feedback visual inmediato
- Diseño totalmente responsive

## 🛠️ Requisitos del Sistema

- Python 3.8+
- MySQL 5.7+
- Redis
- Navegador moderno (Chrome, Firefox, Safari, Edge)

## 🔐 Características de Seguridad

- Validación de tipos de archivo
- Límites de tamaño configurables
- Protección CSRF
- Autenticación segura
- Procesamiento aislado de archivos

## 📋 Buenas Prácticas y Patrones de Diseño

### Arquitectura y Organización
- Separación clara de responsabilidades (patrón MVC)
- Estructura modular por aplicaciones Django
- Configuración separada por entornos
- Sistema de plantillas heredables

### Código Limpio
- Nomenclatura clara y consistente
- Documentación de funciones y clases
- Código DRY (Don't Repeat Yourself)
- Tipado de datos consistente

### Patrones Implementados
- Factory Pattern para procesamiento de imágenes
- Observer Pattern para actualizaciones asíncronas
- Repository Pattern para acceso a datos
- Strategy Pattern para diferentes estrategias de redimensionamiento

### Optimización y Rendimiento
- Procesamiento asíncrono de tareas pesadas
- Caché de resultados frecuentes
- Optimización de consultas a base de datos
- Carga diferida de recursos

### Control de Versiones
- Commits semánticos
- Ramas separadas por funcionalidad
- Documentación de cambios
- Archivos de configuración versionados

