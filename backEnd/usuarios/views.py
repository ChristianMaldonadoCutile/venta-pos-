from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistroSerializer, LoginSerializer, UsuarioSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Privilegio
from .serializers import PrivilegioSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


@api_view(['GET'])
def obtener_todos_los_privilegios(request):
    privilegios = Privilegio.objects.all()
    serializer = PrivilegioSerializer(privilegios, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def obtener_privilegios_por_usuario(request, id_usuario):
    privilegios = Privilegio.objects.filter(usuario_id=id_usuario)
    serializer = PrivilegioSerializer(privilegios, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['POST'])
def crear_privilegio(request):
    serializer = PrivilegioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def cambiar_contraseña(request, pk):
    try:
        usuario = get_user_model().objects.get(pk=pk)
    except get_user_model().DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Verificamos si se proporcionó una nueva contraseña
    nueva_contraseña = request.data.get('nueva_contraseña')
    if not nueva_contraseña:
        return Response({'detail': 'No se proporcionó una nueva contraseña'}, status=status.HTTP_400_BAD_REQUEST)

    # Establecemos la nueva contraseña
    usuario.set_password(nueva_contraseña)
    usuario.save()

    return Response({'detail': 'Contraseña actualizada correctamente'}, status=status.HTTP_200_OK)

# Actualizar los datos del usuario por ID
@api_view(['PUT'])
def actualizar_usuario(request, pk):
    try:
        usuario = get_user_model().objects.get(pk=pk)
    except get_user_model().DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Aquí puedes actualizar los campos del usuario como nombre, rol, estado, etc.
    serializer = UsuarioSerializer(usuario, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistroView(APIView):
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            token, _ = Token.objects.get_or_create(user=usuario)
            return Response({
                'usuario': UsuarioSerializer(usuario).data,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=usuario)
            return Response({
                'usuario': UsuarioSerializer(usuario).data,
                'token': token.key
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
