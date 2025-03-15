// Inicializar lightbox cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    const imagenes = document.querySelectorAll('.thumbnail-preview img, .image-preview img');
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');

    // Configurar eventos para abrir lightbox
    imagenes.forEach(img => {
        img.style.cursor = 'pointer';
        img.addEventListener('click', function() {
            lightboxImg.src = this.src;
            lightbox.style.display = 'block';
        });
    });

    // Cerrar lightbox al hacer click
    lightbox.addEventListener('click', function() {
        this.style.display = 'none';
    });
}); 