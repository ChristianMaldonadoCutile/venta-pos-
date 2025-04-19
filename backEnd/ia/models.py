from django.db import models

# Create your models here.
# ia/models.py
from django.db import models
# ia/models.py
from django.db import models
from productos.models import Producto
from productos.models import NotaVenta, RegistroNotaVenta

class ConversacionCliente(models.Model):
    cliente_id = models.CharField(max_length=100)
    finalizada = models.BooleanField(default=False)
    total_acumulado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descuento_aplicado = models.BooleanField(default=False)

    def __str__(self):
        return f"Conversación con {self.cliente_id}"

class ProductoConversacion(models.Model):
    conversacion = models.ForeignKey(ConversacionCliente, on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"


class Pregunta(models.Model):
    pregunta = models.TextField(unique=True)
    respuesta = models.TextField()

    def __str__(self):
        return self.pregunta
