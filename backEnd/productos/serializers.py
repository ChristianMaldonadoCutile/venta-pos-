from rest_framework import serializers
from productos.models import Producto
from .models import Categoria
from .models import Descuento
from .models import RegistroNotaVenta
from .models import NotaVenta


class RegistroNotaVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroNotaVenta
        fields = '__all__'
        
class NotaVentaSerializer(serializers.ModelSerializer):
    registros = RegistroNotaVentaSerializer(many=True, read_only=True)

    class Meta:
        model = NotaVenta
        fields = '__all__'
class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descuento
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'  # Esto incluye todos los campos del modelo Producto
