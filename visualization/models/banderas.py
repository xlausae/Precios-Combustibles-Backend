from django.db     import models
from .municipios import Municipios


class Banderas(models.Model):
   cod_bandera       = models.AutoField(primary_key=True)
   nom_bandera       = models.CharField('Nombre',max_length=20)
   cod_municipio     = models.ForeignKey(Municipios, related_name='Codigo_Municipio', on_delete=models.CASCADE)
