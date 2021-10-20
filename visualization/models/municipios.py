from django.db    import models
from .departamentos  import Departamentos


class Municipios(models.Model):
    cod_municipio = models.AutoField(primary_key=True)
    nom_municipio = models.CharField('Municipio',max_length=20)
    cod_departamentofk = models.ForeignKey(Departamentos, related_name='Codigo_Departamento',on_delete=models.CASCADE)