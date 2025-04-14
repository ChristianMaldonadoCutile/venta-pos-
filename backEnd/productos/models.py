from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    idproveedor = models.CharField(max_length=100, null=True, blank=True)
    proveedor = models.CharField(max_length=100, null=True, blank=True)
    idcategoria = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.CharField(max_length=100, null=True, blank=True)
    estado = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.nombre
