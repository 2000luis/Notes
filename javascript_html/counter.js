let counter = 0;
function count() {
    counter += 1;
    const h1 = document.querySelector('h1');
    h1.innerHTML = counter;
    if (counter % 10 === 0) {
        alert(`The counter is now: ${counter}`);
    }
}
document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('button').onclick = count;
});

//Lo que pasa en el addEventListener es para poder terminar de cargar la pagina y pueda ver todos los elementos que le siguen a la instrucion que esta unas lineas mas arriba en el html y primero le pasas la propiedad que estas por usar que en este caso es DOMContentLoaded que quiere decir que despues de que termine de cargar el DOM completamente que realize una funcion que es el siegiente parametro que este caso no se le atribuye un nombre ya que solo es usara cuando se ejecute este evento solo se pone function()
//despues de pasa las instrucciones que quieres que realize este evento