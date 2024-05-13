from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import home, categoria_view, herramientas,herramientasE, login,hogar,productos,registro,procesar_pago_view,carrito,maquinaria,materiales,hogar

urlpatterns = [
    path('', home , name="home"),
    path('categoria/<>/', views.categoria_view, name='categoria'),
    path('herramientasE',herramientasE, name="herramientasE"),
    path('herramientas/',herramientas, name="herramientas"),
    path('login/' ,login,  name="login"),
    path('hogar/',hogar , name="hogar"),
    path('productos/',productos, name="productos"),
    path('registro/',registro, name= "registro"),
    path('carrito/', carrito, name="carrito"),
    path('procesar-pago/', procesar_pago_view, name="procesar_pago"),
    path('maquinaria/', maquinaria, name="maquinaria"),
    path('materiales/', materiales, name="materiales"),

    
   
]




   

