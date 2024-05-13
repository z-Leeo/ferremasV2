from django.contrib import admin
from .models import Marca, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca"]
    list_per_page = 5


admin.site.register(Marca)
admin.site.register(Product)