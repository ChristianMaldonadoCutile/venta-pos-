from django.urls import path, include
from .views import RegistroView, LoginView
from . import views
urlpatterns = [
    path('registro/', RegistroView.as_view()),
    path('login/', LoginView.as_view()),
    path('privilegios/crear/', views.crear_privilegio, name='crear_privilegio'),
    path('privilegios/', views.obtener_todos_los_privilegios, name='todos_privilegios'),
    path('privilegios/<int:id_usuario>/', views.obtener_privilegios_por_usuario, name='privilegios_por_usuario'),
    path('cambiar_contraseña/<int:pk>/', views.cambiar_contraseña, name='cambiar_contraseña'),
    path('actualizar_usuario/<int:pk>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('roles/<int:id>/', views.obtener_rol_por_id, name='rol_por_id'),
    path('usuarios/por-rol/<str:name>/', views.obtener_usuarios_por_rol, name='usuarios_por_rol'),
    path('usuarios/todos/', views.obtener_todos_los_usuarios, name='todos_los_usuarios'),
    path('eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
]
urlpatterns += [
    path('roles/crear/', views.crear_rol, name='crear_rol'),
    path('roles/', views.obtener_roles, name='obtener_roles'),
    path('roles/eliminar/<int:id>/', views.eliminar_rol, name='eliminar_rol'),
]


