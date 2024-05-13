from django.db import models

# Create your models here.
class Marca(models.Model):
    idMarca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Product(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="products", null=True)
    def __str__(self):
        return self.nombre
    

class CarritoItem(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    @property
    def total(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"