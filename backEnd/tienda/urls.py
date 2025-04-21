from django.contrib import admin
from django.urls import path, include
from . import views
from ia.views_vendedor import VendedorIAView


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/usuarios/', include('usuarios.urls')),
    # path('api/privilegios/', include('usuarios.urls')),
    path('productos/', include('productos.urls')),
    path('ejecutar_sql/', views.ejecutar_sql, name='ejecutar_sql'),
    path('ejecutar_sql_update/', views.ejecutar_sql_update, name='ejecutar_sql'),
    path('enviar-pregunta/', views.enviar_a_ia, name='enviar_a_ia'),
    path('ia/', include('ia.urls')),
     path('ia/vendedor/', VendedorIAView.as_view(), name='vendedor_ia'),
]
