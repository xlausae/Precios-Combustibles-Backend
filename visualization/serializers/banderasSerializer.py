from visualization.models.banderas import Banderas
from rest_framework                import serializers

class BanderasSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Banderas
        fields = ['nom_bandera']
    def to_representation(self,obj):
        marca  = Banderas.objects.get(id=obj.id)
        return {
            'nombre' : marca.nom_bandera
        }