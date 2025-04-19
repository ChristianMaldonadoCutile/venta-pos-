from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from productos.models import Producto, NotaVenta, RegistroNotaVenta
from ia.models import ConversacionCliente, ProductoConversacion
from django.utils import timezone
from decimal import Decimal
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

class VendedorIAView(APIView):
    def post(self, request):
        cliente_id = request.data.get('cliente_id')
        mensaje = request.data.get('pregunta')

        if not cliente_id or not mensaje:
            return Response({"error": "Faltan datos"}, status=400)

        # Obtener o crear conversación activa
        conversacion, _ = ConversacionCliente.objects.get_or_create(
            cliente_id=cliente_id, finalizada=False,
            defaults={'total_acumulado': 0, 'descuento_aplicado': False}
        )

        # Obtener historial de conversación
        historial = ProductoConversacion.objects.filter(conversacion=conversacion)
        historial_texto = "\n".join([
            f"Producto: {h.producto.nombre}, Cantidad: {h.cantidad}" for h in historial
        ])

        # Crear el prompt para Mistral
        prompt = f"""
Eres un vendedor experto de una tienda de electrónicos. El cliente dice: "{mensaje}".

Historial de compra:
{historial_texto or 'Sin productos aún.'}

Tu tarea es responder de forma natural y amigable. Si el cliente menciona un producto, pregúntale si desea reservarlo. Si confirma, regístralo. Si quiere finalizar la compra, indícalo como acción.

Responde en formato JSON:
{{
    "respuesta": "mensaje amigable para el cliente",
    "accion": "ninguna | preguntar_reserva | añadir_producto | finalizar_compra | actualizar_tipo_venta | solicitar_direccion",
    "producto": "nombre del producto (opcional)",
    "confirmado": true/false (si es añadir producto),
    "tipo_venta": "envio | recoger" (si aplica),
    "direccion": "si aplica"
}}
"""

        # Llamada a Mistral vía Ollama
        response = requests.post(OLLAMA_URL, json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        })

        respuesta_ia = response.json()["response"]
        try:
            data = json.loads(respuesta_ia)
        except json.JSONDecodeError:
            return Response({"respuesta": "Hubo un error interpretando la respuesta del vendedor. ¿Puedes repetir?"})

        accion = data.get("accion")
        producto_nombre = data.get("producto")
        respuesta = data.get("respuesta", "¡Gracias por tu mensaje!")
        confirmado = data.get("confirmado", False)
        tipo_venta = data.get("tipo_venta")
        direccion = data.get("direccion")

        if accion == "añadir_producto" and confirmado and producto_nombre:
            try:
                producto = Producto.objects.get(nombre__iexact=producto_nombre, estado=True)
                ProductoConversacion.objects.get_or_create(
                    conversacion=conversacion,
                    producto=producto,
                    defaults={"cantidad": 1}
                )
                conversacion.total_acumulado += Decimal(producto.precio)
                conversacion.save()
                respuesta += f" Se ha reservado 1 {producto.nombre} para ti."
            except Producto.DoesNotExist:
                respuesta += f" No tenemos {producto_nombre} disponible ahora mismo."

        elif accion == "finalizar_compra":
            registros = ProductoConversacion.objects.filter(conversacion=conversacion)
            total = conversacion.total_acumulado
            descuento_bs = 0

            if total >= 1000 and not conversacion.descuento_aplicado:
                descuento_bs = total * Decimal("0.10")
                total -= descuento_bs
                conversacion.descuento_aplicado = True
                conversacion.save()

            nota = NotaVenta.objects.create(
                total=conversacion.total_acumulado,
                descuento=descuento_bs,
                total_pago=total,
                tipo_venta="por_definir",
                tipo_pago="efectivo",
                estado="pendiente",
                fecha=timezone.now().date(),
                hora=timezone.now().time(),
                cliente_id=cliente_id
            )

            for registro in registros:
                RegistroNotaVenta.objects.create(
                    nota=nota,
                    producto=registro.producto,
                    nombre_producto=registro.producto.nombre,
                    costo=registro.producto.precio,
                    estado="vendido"
                )
                registro.producto.cantidad -= 1
                registro.producto.save()

            conversacion.finalizada = True
            conversacion.save()
            respuesta += f" Tu compra ha sido registrada. Total: {total:.2f} Bs."

        elif accion == "actualizar_tipo_venta" and tipo_venta:
            ultima_nota = NotaVenta.objects.filter(cliente_id=cliente_id).order_by('-id').first()
            if ultima_nota:
                ultima_nota.tipo_venta = tipo_venta
                ultima_nota.save()
                respuesta += f" Tipo de entrega actualizado a: {tipo_venta}."

        elif accion == "solicitar_direccion" and direccion:
            ultima_nota = NotaVenta.objects.filter(cliente_id=cliente_id).order_by('-id').first()
            if ultima_nota:
                ultima_nota.direccion = direccion
                ultima_nota.save()
                respuesta += f" Dirección registrada correctamente."

        return Response({"respuesta": respuesta})
