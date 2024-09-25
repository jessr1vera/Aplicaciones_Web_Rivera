// Script para manejar los detalles del producto
document.addEventListener("DOMContentLoaded", function() {
    const params = new URLSearchParams(window.location.search);
    const producto = params.get('producto');
    
    const detalles = {
        'starface': {
            'nombre': 'Starface Hydro-Star',
            'descripcion': 'Parches de espinillas de ácido salicílico y Big Blue Compact.',
            'imagen': 'assets/producto1.jpg'
        },
        'whipped': {
            'nombre': 'Whipped Cream',
            'descripcion': 'Crema hidratante rica y nutritiva diseñada para restaurar y fortalecer la barrera de la piel.',
            'imagen': 'assets/producto2.jpg'
        },
        'plump-plum': {
            'nombre': 'Plump Plum Hyaluronic Serum',
            'descripcion': 'Sérum facial diseñado para ofrecer una hidratación intensa.',
            'imagen': 'assets/producto3.jpg'
        },
        'lip-sleeping': {
            'nombre': 'Lip Sleeping Mask',
            'descripcion': 'Tratamiento intensivo para labios diseñado para hidratar, nutrir y suavizar.',
            'imagen': 'assets/producto4.jpg'
        }
    };

    if (producto && detalles[producto]) {
        document.getElementById('producto-nombre').innerText = detalles[producto].nombre;
        document.getElementById('producto-descripcion').innerText = detalles[producto].descripcion;
        document.getElementById('producto-imagen').src = detalles[producto].imagen;
    } else {
        document.getElementById('producto-nombre').innerText = 'Producto no encontrado';
        document.getElementById('producto-descripcion').innerText = '';
        document.getElementById('producto-imagen').src = '';
    }
});

// Función para manejar el envío del formulario de compra
document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("compraForm");

    if (form) {
        form.addEventListener("submit", function(event) {
            event.preventDefault(); // Evita que el formulario se envíe de forma predeterminada
            
            const cantidad = parseInt(document.getElementById("cantidad").value);
            const precioPorUnidad = parseFloat(document.getElementById("precio").value);
            const total = cantidad * precioPorUnidad;

            alert(`Total a pagar: $${total.toFixed(2)}`);
        });
    }
});
