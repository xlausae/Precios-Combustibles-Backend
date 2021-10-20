from visualization.models.tipo_productos import Tipo_productos
from rest_framework                      import serializers

class Tipo_productosSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Tipo_productos
        fields = ['nom_tipo_producto']
    def to_representation(self,obj):
        product  = Tipo_productos.objects.get(id=obj.id)
        return {
            'nombre' : product.nom_tipo_producto
        }