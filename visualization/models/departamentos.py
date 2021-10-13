from django.db import models


class Departamentos(models.Model):
   cod_departamento = models.AutoField(primary_key=True)
   nom_departamento = models.CharField('Departamento',max_length=20) 