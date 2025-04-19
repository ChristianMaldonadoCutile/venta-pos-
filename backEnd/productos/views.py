from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from productos.models import Producto
from productos.serializers import ProductoSerializer
from .models import Categoria
from .serializers import CategoriaSerializer
from rest_framework import viewsets
from .models import Descuento
from .serializers import DescuentoSerializer
from .serializers import RegistroNotaVentaSerializer
from .serializers import NotaVentaSerializer
from .models import NotaVenta
from .models import RegistroNotaVenta


@api_view(['GET'])
def obtener_nota_con_productos(request, pk):
    try:
        nota = NotaVenta.objects.get(pk=pk)
        registros = RegistroNotaVenta.objects.filter(nota_venta=nota)

        nota_serializada = NotaVentaSerializer(nota)
        registros_serializados = RegistroNotaVentaSerializer(registros, many=True)

        data = {
            'nota': nota_serializada.data,
            'registros': registros_serializados.data
        }
        return Response(data)
    except NotaVenta.DoesNotExist:
        return Response({'error': 'Nota de venta no encontrada'}, status=404)

class NotaVentaViewSet(viewsets.ModelViewSet):
    queryset = NotaVenta.objects.all()
    serializer_class = NotaVentaSerializer

class RegistroNotaVentaViewSet(viewsets.ModelViewSet):
    queryset = RegistroNotaVenta.objects.all()
    serializer_class = RegistroNotaVentaSerializer

class DescuentoViewSet(viewsets.ModelViewSet):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer



@api_view(['POST'])
def crear_categoria(request):
    serializer = CategoriaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def obtener_categorias(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def obtener_categoria_por_id(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return Response({'error': 'Categoría no encontrada'}, status=404)
    serializer = CategoriaSerializer(categoria)
    return Response(serializer.data)

@api_view(['PUT'])
def actualizar_categoria(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return Response({'error': 'Categoría no encontrada'}, status=404)
    serializer = CategoriaSerializer(categoria, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def eliminar_categoria(request, id):
    try:
        categoria = Categoria.objects.get(id=id)
        categoria.delete()
        return Response({'detail': 'Rol eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)
    except Categoria.DoesNotExist:
        return Response({'detail': 'Rol no encontrado'}, status=status.HTTP_404_NOT_FOUND)


# Crear Producto
@api_view(['POST'])
def crear_producto(request):
    if request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtener Producto por ID
@api_view(['GET'])
def obtener_producto(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductoSerializer(producto)
    return Response(serializer.data)

# Obtener Todos los Productos
@api_view(['GET'])
def obtener_productos(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)

# Actualizar Producto
@api_view(['PUT'])
def actualizar_producto(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductoSerializer(producto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_producto(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)