// Para la vista previa de imágenes
document.addEventListener('DOMContentLoaded', function() {
    const inputImagen = document.querySelector('input[type="file"]');
    const previewDiv = document.querySelector('#image-preview');

    inputImagen.addEventListener('change', function() {
        const archivo = this.files[0];
        if (archivo) {
            const reader = new FileReader();
            
            reader.onload = function(e) {
                const img = new Image();
                img.src = e.target.result;
                
                img.onload = function() {
                    previewDiv.innerHTML = `
                        <div style="position: relative;">
                            <img src="${e.target.result}" 
                                 style="max-width: 300px; 
                                        border-radius: 8px; 
                                        margin-top: 10px; 
                                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                            <button type="button" 
                                    onclick="limpiarSeleccion()"
                                    style="position: absolute; 
                                           top: 15px; 
                                           right: 5px; 
                                           background: #ff4444; 
                                           color: white; 
                                           border: none; 
                                           border-radius: 50%; 
                                           width: 25px; 
                                           height: 25px; 
                                           cursor: pointer;">×</button>
                            <p style="margin-top: 10px; 
                                     color: #666; 
                                     font-size: 14px;">
                                Dimensiones: ${this.width}px × ${this.height}px
                            </p>
                        </div>
                    `;
                }
            }
            
            reader.readAsDataURL(archivo);
        } else {
            previewDiv.innerHTML = '';
        }
    });
});

function limpiarSeleccion() {
    const inputImagen = document.querySelector('input[type="file"]');
    const previewDiv = document.querySelector('#image-preview');
    inputImagen.value = '';
    previewDiv.innerHTML = '';
} 