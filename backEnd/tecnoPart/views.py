from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def ejecutar_sql(request):
    sql = request.data.get('sql_query')  # Asegúrate de recibir la consulta de manera controlada
    
    if not sql:
        return Response({'detail': 'No se proporcionó consulta SQL'}, status=400)
    
    # Validamos y preparamos la consulta para evitar inyecciones SQL (evitar SQL dinámico sin controles)
    if 'DROP' in sql or 'DELETE' in sql:
        return Response({'detail': 'Operaciones peligrosas no permitidas'}, status=400)
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            # Suponiendo que la consulta es SELECT
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]  # Obtener nombres de las columnas
            result = [dict(zip(columns, row)) for row in rows]
            return Response(result)
    except Exception as e:
        return Response({'detail': str(e)}, status=500)

@api_view(['POST'])
def ejecutar_sql_update(request):
    sql = request.data.get('sql_query')  # Asegúrate de recibir la consulta de manera controlada
    
    if not sql:
        return Response({'detail': 'No se proporcionó consulta SQL'}, status=400)
    
    # Validamos y preparamos la consulta para evitar inyecciones SQL (evitar SQL dinámico sin controles)
    if 'DROP' in sql or 'DELETE' in sql:
        return Response({'detail': 'Operaciones peligrosas no permitidas'}, status=400)
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)  # Ejecutar la consulta SQL
            # Si la consulta es un UPDATE, puedes obtener el número de filas afectadas
            if cursor.rowcount > 0:
                return Response({'detail': f'Operación exitosa. {cursor.rowcount} filas afectadas.'})
            else:
                return Response({'detail': 'No se encontraron filas para actualizar.'})
    except Exception as e:
        return Response({'detail': str(e)}, status=500)