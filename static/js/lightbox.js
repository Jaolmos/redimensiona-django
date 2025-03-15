document.addEventListener('DOMContentLoaded', function() {
    const imagenes = document.querySelectorAll('.thumbnail-preview img, .image-preview img');
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');

    imagenes.forEach(img => {
        img.style.cursor = 'pointer';
        img.addEventListener('click', function() {
            lightboxImg.src = this.src;
            lightbox.style.display = 'block';
        });
    });

    lightbox.addEventListener('click', function() {
        this.style.display = 'none';
    });
}); 