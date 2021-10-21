from django.db import models
from .banderas import Banderas


class Estaciones(models.Model):
    cod_estacion = models.AutoField(primary_key=True)
    nom_estacion = models.CharField('Nombre_Estación',max_length=30)
    dir_estacion = models.CharField('Direccion',max_length=30)
    cod_bandera  = models.ForeignKey(Banderas, related_name='Empresa',on_delete=models.CASCADE)
