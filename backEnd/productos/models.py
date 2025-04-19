from django.db import models



class NotaVenta(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    descuento_tipo = models.ForeignKey('Descuento', null=True, blank=True, on_delete=models.SET_NULL)
    descuento_cantidad = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    total_pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    nit = models.CharField(max_length=20, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    hora = models.TimeField(null=True, blank=True)
    usuario = models.ForeignKey('usuarios.Usuario', null=True, blank=True, on_delete=models.SET_NULL, related_name='ventas_usuario')
    empleado = models.ForeignKey('usuarios.Usuario', null=True, blank=True, on_delete=models.SET_NULL, related_name='ventas_empleado')
    tipo_venta = models.CharField(max_length=50, choices=[('online', 'Online'), ('fisica', 'En tienda física')], null=True, blank=True)
    tipo_pago = models.CharField(max_length=50, choices=[('efectivo', 'Efectivo'), ('qr', 'QR')], null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    estado = models.BooleanField(default=True)
    
class RegistroNotaVenta(models.Model):
    nota_venta = models.ForeignKey(NotaVenta, related_name='registros', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)

class Descuento(models.Model):
    nombre = models.CharField(max_length=100)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    idcategoria = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.CharField(max_length=100, null=True, blank=True)
    estado = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.nombre
