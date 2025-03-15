// Para la vista previa de imágenes
document.addEventListener('DOMContentLoaded', function() {
    const inputImagen = document.querySelector('input[type="file"]');
    const previewDiv = document.querySelector('#image-preview');
    const inputAlto = document.querySelector('input[name="custom_height"]');
    const inputAncho = document.querySelector('input[name="custom_width"]');
    let aspectRatio = 0; // Proporción de la imagen

    // Cuando se seleccione una imagen
    inputImagen.addEventListener('change', function() {
        const archivo = this.files[0];
        if (archivo) {
            const reader = new FileReader();
            
            reader.onload = function(e) {
                const img = new Image();
                img.src = e.target.result;
                
                img.onload = function() {
                    // Guardar la proporción de la imagen
                    aspectRatio = this.width / this.height;
                    
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

    // Calcular alto cuando se introduce ancho
    inputAncho.addEventListener('input', function() {
        if (aspectRatio && this.value) {
            const nuevoAlto = Math.round(this.value / aspectRatio);
            inputAlto.value = nuevoAlto;
        } else {
            inputAlto.value = '';
        }
    });

    // Calcular ancho cuando se introduce alto
    inputAlto.addEventListener('input', function() {
        if (aspectRatio && this.value) {
            const nuevoAncho = Math.round(this.value * aspectRatio);
            inputAncho.value = nuevoAncho;
        } else {
            inputAncho.value = '';
        }
    });
});

function limpiarSeleccion() {
    const inputImagen = document.querySelector('input[type="file"]');
    const previewDiv = document.querySelector('#image-preview');
    const inputAlto = document.querySelector('input[name="custom_height"]');
    const inputAncho = document.querySelector('input[name="custom_width"]');
    inputImagen.value = '';
    previewDiv.innerHTML = '';
    inputAlto.value = '';
    inputAncho.value = '';
} 