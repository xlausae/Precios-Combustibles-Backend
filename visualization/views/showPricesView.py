from django.conf                                              import settings
from rest_framework                                           import generics, status
from rest_framework.response                                  import Response
from rest_framework.permissions                               import IsAuthenticated

from visualization.models.estaciones_productos                import Estaciones_productos
from visualization.serializers.estaciones_productosSerializer import Estaciones_productosSerializer


class ShowPricesView(generics.ListAPIView):
    queryset           = Estaciones_productos.objects.all()
    serializer_class   = Estaciones_productosSerializer
    permission_classes = (IsAuthenticated, )
    
    def get(self,request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

