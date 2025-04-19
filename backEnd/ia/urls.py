# ia/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('entrenar/', views.entrenar, name='entrenar_ia'),
    path('preguntar/', views.preguntar, name='preguntar_ia'),
]
