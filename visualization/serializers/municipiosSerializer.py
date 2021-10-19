from visualization.models.municipios   import Municipios
from rest_framework                    import serializers

class MunicipiosSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Municipios
        fields = ['nom_municipio']
    def to_representation(self,obj):
        mun  = Municipios.objects.get(id=obj.id)
        return {
            'nombre' : mun.nom_municipio
        }