from django.conf                        import settings
from rest_framework                     import generics, status, views
from rest_framework.response            import Response
from visualization.serializers.estaciones_productosSerializer import Estaciones_productosSerializer
from visualization.models.estaciones_productos    import Estaciones_productos

class EstacionesProductosDetailView(generics.RetrieveAPIView):
    serializer_class = Estaciones_productosSerializer
    queryset = Estaciones_productos.objects.all()

class EstacionesProductosCreateView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = Estaciones_productosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        dat = {
            "periodo": request.data['periodo'],
            "mes": request.data['mes'],
            "precio": request.data['precio'],
            "estado": request.data['estado'],
            "cod_estacion": request.data['cod_estacion'],
            "cod_tipo_producto": request.data['cod_tipo_producto']
        }

        estacionProducto = Estaciones_productos.objects.get(data=dat)
        estacionProducto.save()

        return Response("Registro exitoso", status=status.HTTP_201_CREATED)

class EstacionesProductosDeleteView(generics.DestroyAPIView):
    serializer_class = Estaciones_productosSerializer
    queryset = Estaciones_productos.objects.all()

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
