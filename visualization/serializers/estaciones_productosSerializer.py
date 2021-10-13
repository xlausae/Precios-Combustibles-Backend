from visualization.models.estaciones_productos import Estaciones_productos
from visualization.models.estaciones           import Estaciones
from visualization.models.tipo_productos       import Tipo_productos

from rest_framework                            import serializers

class Estaciones_productosSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Estaciones_productos
        fields = ['periodo', 'mes', 'precio', 'estado', 'cod_estacion', 'cod_tipo_producto']

    def to_representation(self,obj):
        precios  = Estaciones_productos.objects.get(id=obj.id)
        estacion = Estaciones.objects.get(id=obj.cod_estacion)
        producto = Tipo_productos.objects.get(id=obj.cod_tipo_producto)
        return {
            'periodo'  : precios.periodo,
            'mes'      : precios.mes,
            'precio'   : precios.precio,
            'estado'   : precios.estado,
            'estacion' : estacion.nom_estacion,
            'direccion': estacion.dir_estacion,
            'producto' : producto.nom_tipo_producto
        }
