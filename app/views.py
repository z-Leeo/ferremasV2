from django.shortcuts import render
from django.shortcuts import render
from .models import Product 
import json
from django.http import JsonResponse
    

def convert_currency(request):
    amount = float(request.GET.get('amount', 0))
    from_currency = request.GET.get('from_currency', '')
    to_currency = request.GET.get('to_currency', '')

    # Cargar las tasas de cambio desde el archivo JSON
    with open('currencies.json') as f:
        exchange_rates = json.load(f)

    if from_currency in exchange_rates and to_currency in exchange_rates:
        converted_amount = amount * exchange_rates[from_currency] / exchange_rates[to_currency]
        return JsonResponse({'converted_amount': converted_amount})
    else:
        return JsonResponse({'error': 'Monedas no válidas'})

def home(request):
    return render(request, 'app/home.html')

def herramientasE(request):
    return render(request, 'app/herramientasE.html')

def herramientas(request):
    return render(request,'app/herramientas.html')

def categoria(request):
    return render(request, 'app/categoria.html')

def login(request):
    return render(request, 'app/login.html')

def hogar(request):
    return render(request, 'app/hogar.html')

def productos(request):
    productos = Product.objects.all()
    data = {
        'productos': productos
    }
    return render(request,'app/productos.html',data)

def registro(request):
    return render(request, 'app/registro.html')
def carrito(request):
    return render(request, 'app/carrito.html')

def maquinaria(request):
    return render(request,'app/maquinaria.html')

def materiales(request):
    return render(request,'app/materiales.html')

def carrito(request):

    
    # Renderizar la plantilla del carrito con los datos del carrito y el total
    return render(request, 'app/carrito.html')

def procesar_pago_view(request):
    return render(request,'app/carrito_view')

def product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'product_details.html', context)



def carrito(request):
    carrito = CarritoItem.objects.filter(usuario=request.user)  # Suponiendo que tengas un campo 'usuario' en tu modelo CarritoItem
    total_carrito = sum(item.total for item in carrito)
    return render(request, 'carrito.html', {'carrito': carrito, 'total_carrito': total_carrito})