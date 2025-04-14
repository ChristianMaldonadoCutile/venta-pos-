from django.urls import path
from productos import views

urlpatterns = [
    path('crear/', views.crear_producto, name='crear_producto'),
    path('obtener/<int:pk>/', views.obtener_producto, name='obtener_producto'),
    path('obtener_todos/', views.obtener_productos, name='obtener_productos'),
    path('actualizar/<int:pk>/', views.actualizar_producto, name='actualizar_producto'),
]
