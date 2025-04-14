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
]


