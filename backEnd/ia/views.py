# ia/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Pregunta
from .serializers import PreguntaSerializer

OLLAMA_API = "http://localhost:11434/api/generate"

CONTEXT = """
Eres un asistente de pedidos para el restaurante King. Tu trabajo es atender a los clientes amablemente, como si fueras un mesero virtual.
Tu rol es:
- Saludar según la hora (buenos días, buenas tardes, buenas noches).
- Preguntar qué desea ordenar.
- Si pide un plato como "pollo", ofrecer una bebida.
- Si acepta, preguntar qué tamaño de bebida desea (pequeña, mediana, grande).
- Ofrecer algo adicional, como postre o promociones.
- Si el cliente pregunta por promociones, dile que hay una promoción de "dos pollos con dos gaseosas pequeñas y un postre".
- Responde solo sobre saludos, menú, promociones y pedidos. No respondas temas fuera del restaurante.
El horario de atención es de 18:00 a 23:00.
"""

@api_view(['POST'])
def entrenar(request):
    serializer = PreguntaSerializer(data=request.data)
    if serializer.is_valid():
        pregunta = serializer.validated_data['pregunta']
        if Pregunta.objects.filter(pregunta__iexact=pregunta).exists():
            return Response({"error": "Esta pregunta ya está registrada"}, status=409)
        serializer.save()
        return Response({"mensaje": "Pregunta guardada correctamente"}, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def preguntar(request):
    cliente_id = request.data.get("cliente_id")
    pregunta = request.data.get("pregunta")

    if not cliente_id or not pregunta:
        return Response({"error": "Faltan datos"}, status=400)

    preguntas = Pregunta.objects.all()
    contexto_extra = "\n\n".join([f"Pregunta: {p.pregunta}\nRespuesta: {p.respuesta}" for p in preguntas])

    prompt = f"""
Contexto del restaurante:
{CONTEXT}

{contexto_extra}

Cliente dice: {pregunta}

Responde como si fueras el mesero del restaurante.
"""

    try:
        r = requests.post(OLLAMA_API, json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        })

        data = r.json()
        return Response({"respuesta": data.get("response")})
    except Exception as e:
        return Response({"error": f"Error al conectar con Ollama: {str(e)}"}, status=500)
