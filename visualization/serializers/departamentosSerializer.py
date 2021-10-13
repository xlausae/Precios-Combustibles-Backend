from visualization.models.departamentos import Departamentos
from rest_framework                     import serializers

class DepartamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Departamentos
        fields = ['nom_departamento']
    def to_representation(self,obj):
        department  = Departamentos.objects.get(id=obj.id)
        return {
            'nombre' : department.nom_departamento
        }