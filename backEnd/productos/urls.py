from django.urls import include, path
from productos import views
from rest_framework.routers import DefaultRouter
from .views import DescuentoViewSet
from rest_framework.routers import DefaultRouter
from .views import NotaVentaViewSet, RegistroNotaVentaViewSet, obtener_nota_con_productos
from .views import (
    NotaVentaViewSet,
    RegistroNotaVentaViewSet,
    DescuentoViewSet,
    obtener_nota_con_productos
)
router = DefaultRouter()
router.register('notas', NotaVentaViewSet, basename='notas')
router.register('registros', RegistroNotaVentaViewSet, basename='registros')
router.register('descuentos', DescuentoViewSet, basename='descuento')


urlpatterns= [
    path('nota-con-productos/<int:pk>/', obtener_nota_con_productos, name='nota_con_productos'),
    path('productos/', include(router.urls)),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('obtener/<int:pk>/', views.obtener_producto, name='obtener_producto'),
    path('obtener_todos/', views.obtener_productos, name='obtener_productos'),
    path('actualizar/<int:pk>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/', views.obtener_categorias, name='obtener_categorias'),
    path('categorias/<int:pk>/', views.obtener_categoria_por_id, name='categoria_por_id'),
    path('categorias/actualizar/<int:pk>/', views.actualizar_categoria, name='actualizar_categoria'),
    path('categorias/eliminar/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),
]
