const container = document.querySelector(".container");
const primaryNav = document.querySelector(".nav__list");
const toggleButton = document.querySelector(".nav-toggle");

toggleButton.addEventListener("click", () => {
    const isExpanded = primaryNav.getAttribute("aria-expanded");
    primaryNav.setAttribute(
        "aria-expanded",
        isExpanded === "false" ? "true" : "false"
    );
});

container.addEventListener("click", (e) => {
    if (!primaryNav.contains(e.target) && !toggleButton.contains(e.target)) {
        primaryNav.setAttribute("aria-expanded", "false");
    }
});

const mainCarousel = new Carousel(document.querySelector("#mainCarousel"), {
    Dots: false,
  });

  const navCarousel = new Carousel(document.querySelector("#navCarousel"), {
    Sync: {
      target: mainCarousel,
    },
    Dots: false,
    Navigation: false,

    infinite: false,
    center: true,
    slidesPerPage: 1,
  });
//api

//Agregar al carro
function agregarAlCarritoAjax(nombreProducto, precioProducto) {
  // Realizar una solicitud AJAX al servidor para agregar el producto al carrito
  // Ejemplo con jQuery:
  $.ajax({
      url: 'carrito',
      type: 'POST',
      data: {
          nombre_producto: nombreProducto,
          precio_producto: precioProducto
      },
      success: function(response) {
          // Manejar la respuesta del servidor (por ejemplo, actualizar la interfaz de usuario)
          alert(`Producto ${nombreProducto} agregado al carrito por $${precioProducto}`);
      },
      error: function(error) {
          console.error('Error al agregar al carrito:', error);
      }
  });
}