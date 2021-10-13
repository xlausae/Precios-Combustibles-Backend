from visualization.models.estaciones import Estaciones
from rest_framework                  import serializers

class EstacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Estaciones
        fields = ['nom_estacion', 'dir_estacion']
    def to_representation(self,obj):
        station  = Estaciones.objects.get(id=obj.id)
        return {
            'nombre'   : station.nom_estacion,
            'direccion': station.dir_estacion
        }