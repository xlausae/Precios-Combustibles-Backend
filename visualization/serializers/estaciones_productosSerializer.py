from visualization.models.estaciones_productos import Estaciones_productos
from visualization.models.estaciones           import Estaciones
from visualization.models.tipo_productos       import Tipo_productos

from rest_framework                            import serializers

class Estaciones_productosSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Estaciones_productos
        fields = ['id_estacion_producto','periodo', 'mes', 'precio', 'estado','cod_estacion', 'cod_tipo_producto']
        def create(self, validated_data):
            estacion = Estaciones_productos.objects.create(**validated_data)
            return estacion

        def to_representation(self,obj):
            estacion = Estaciones.objects.get(id=obj.cod_estacion)
            return {
                'periodo'  : estacion.periodo,
                'mes'      : estacion.mes,
                'precio'   : estacion.precio,
                'estado'   : estacion.estado,
                'estacion' : estacion.cod_estacion,
                'producto' : estacion.cod_tipo_producto
            }
