# ia/serializers.py
from rest_framework import serializers
from .models import Pregunta

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'
