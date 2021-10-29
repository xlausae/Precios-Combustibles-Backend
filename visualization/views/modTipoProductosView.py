from django.conf                        import settings
from rest_framework                     import generics, status, views
from rest_framework.response            import Response
from visualization.serializers.tipo_productosSerializer import Tipo_productosSerializer
from visualization.models.tipo_productos    import Tipo_productos

class TipoProductoCreateView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):

        serializer = Tipo_productosSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TipoProductoDetailView(generics.RetrieveAPIView):
    serializer_class = Tipo_productosSerializer
    queryset = Tipo_productos.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoProductoUpdateView(generics.UpdateAPIView):
    serializer_class = Tipo_productosSerializer
    queryset = Tipo_productos.objects.all()

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class TipoProductoDeleteView(generics.DestroyAPIView):
    serializer_class = Tipo_productosSerializer
    queryset = Tipo_productos.objects.all()

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
