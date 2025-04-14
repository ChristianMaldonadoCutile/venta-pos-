from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/usuarios/', include('usuarios.urls')),
    path('api/privilegios/', include('usuarios.urls')),
    path('productos/', include('productos.urls')),
    path('ejecutar_sql/', views.ejecutar_sql, name='ejecutar_sql'),
    path('ejecutar_sql_update/', views.ejecutar_sql_update, name='ejecutar_sql')
]
