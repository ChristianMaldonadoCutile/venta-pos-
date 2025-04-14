from rest_framework import serializers
from .models import Usuario
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Privilegio

class PrivilegioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privilegio
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email', 'rol', 'nit', 'estado']

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'rol', 'nit', 'estado', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return Usuario.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        usuario = authenticate(**data)
        if usuario and usuario.estado:
            return usuario
        raise serializers.ValidationError("Credenciales incorrectas o usuario inactivo.")
