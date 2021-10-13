from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from visualization.models.estaciones_productos import Estaciones_productos
from visualization.serializers.estaciones_productosSerializer import Estaciones_productosSerializer

class AllStationsView(APIView):
    def get(self, request):
        todos = Estaciones_productos.objects.all()
        serializer_class = Estaciones_productosSerializer(todos, many = True)

        return Response(serializer_class.data)
