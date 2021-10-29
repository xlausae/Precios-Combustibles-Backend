from visualization.models.tipo_productos import Tipo_productos
from rest_framework                      import serializers

class Tipo_productosSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Tipo_productos
        fields = ['cod_tipo_producto' ,'nom_tipo_producto']
        
    def to_representation(self,obj):
        product  = Tipo_productos.objects.get(cod_tipo_producto=obj.cod_tipo_producto)
        #product1  = Tipo_productos.objects.get(nom_tipo_producto=obj.nom_tipo_producto)
        return {
            'cod_tipo_producto' : product.cod_tipo_producto,
            'nom_tipo_producto' : product.nom_tipo_producto
        }