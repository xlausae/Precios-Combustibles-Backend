from visualization.models.municipios   import Municipios
from rest_framework                    import serializers

class MunicipiosSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Municipios
        fields = ['nom_municipio','cod_departamentofk']
    def to_representation(self,obj):
        mun  = Municipios.objects.get(cod_municipio=obj.cod_municipio)
        return {
            'nombre' : mun.nom_municipio
        }