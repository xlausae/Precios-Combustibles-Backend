from django.db import models
from .estaciones import Estaciones
from .tipo_productos import Tipo_productos


class Estaciones_productos(models.Model):
    id_estacion_producto = models.AutoField(primary_key=True)
    periodo              = models.DateField()
    mes                  = models.DateField()
    precio               = models.IntegerField(default=0)
    estado               = models.BooleanField()
    cod_estacion         = models.ForeignKey(Estaciones, related_name='Codigo_Estación', on_delete=models.CASCADE)
    cod_tipo_producto    = models.ForeignKey(Tipo_productos,related_name='Codigo_Producto', on_delete=models.CASCADE)