from visualization.models.estaciones import Estaciones
from rest_framework                  import serializers

class EstacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Estaciones
        fields = ['cod_estacion','nom_estacion', 'dir_estacion', 'cod_bandera']

    def to_representation(self,obj):
        station  = Estaciones.objects.get(cod_estacion=obj.cod_estacion)
        return {
            'cod_estacion': station.cod_estacion,
            'nombre'   : station.nom_estacion,
            'direccion': station.dir_estacion,
            'cod_bandera' : station.cod_bandera
        }