from django.conf                        import settings
from rest_framework                     import status, views, generics
from rest_framework.response            import Response
from visualization.serializers.estacionesSerializer import EstacionesSerializer
from visualization.models.estaciones    import Estaciones


class StationCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = EstacionesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED) 

class StationDeleteView(generics.DestroyAPIView):
    serializer_class = EstacionesSerializer
    queryset = Estaciones.objects.all()

    def get(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
