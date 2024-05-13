from django.shortcuts import render
from django.shortcuts import render
from .models import Product
import json

    
def home(request):
    return render(request, 'app/home.html')

def herramientasE(request):
    return render(request, 'app/herramientasE.html')

def herramientas(request):
    return render(request,'app/herramientas.html')

def categoria_view(request):
    return render(request, 'app/categoria.html')

def login(request):
    return render(request, 'app/login.html')

def hogar(request):
    return render(request, 'app/hogar.html')

def productos(request):
    return render(request,'app/productos.html')

def registro(request):
    return render(request, 'app/registro.html')
def carrito(request):
    return render(request, 'app/carrito.html')

def maquinaria(request):
    return render(request,'app/maquinaria.html')

def materiales(request):
    return render(request,'app/materiales.html')

def carrito_view(request):
    # Obtener el carrito de la sesión del usuario
    carrito = request.session.get('carrito', [])
    
    # Calcular el total del carrito sumando los precios de los productos
    total = sum(producto.get('precio', 0) for producto in carrito)
    
    # Renderizar la plantilla del carrito con los datos del carrito y el total
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})

def procesar_pago_view(request):
    return render(request,'app/carrito_view')