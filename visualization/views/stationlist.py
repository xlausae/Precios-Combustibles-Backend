from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from visualization.models.departamentos import Departamentos
from visualization.models.municipios import Municipios
from visualization.models.estaciones import Estaciones
from visualization.serializers.departamentosSerializer import DepartamentosSerializer
from visualization.serializers.municipiosSerializer import MunicipiosSerializer
from visualization.serializers.estacionesSerializer import EstacionesSerializer

class Municipioslist(APIView):
    def get(self, request):
        MunicipiosSelect = Municipios.objects.only('nom_municipio').filter(cod_departamentofk= request.data)
        serializer_class = municipiosSerializer(MunicipiosSelect, many = True)

        return Response(serializer_class.data)

class Stationslist(APIView):
    def get(self, request):
        StationSelect = Estaciones.objects.only('nom_estacion').filter(cod_municipiofk=request.data)
        serializer_class = estacionesSerializer(StationSelect, many = True)

        return Response(serializer_class.data)

class Departamentolist(APIView):
    def get (self,request):
        DepartamentoSelect= Departamentos.objects.only('nom_departamento')
        serializer_class = departamentosSerializer(DepartamentoSelect, many = True)
        
        return Response(serializer_class.data)
    

    


        
     