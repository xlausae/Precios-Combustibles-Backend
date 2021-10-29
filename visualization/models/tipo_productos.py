from django.db import models

class Tipo_productos(models.Model):
    cod_tipo_producto = models.AutoField(primary_key=True)
    nom_tipo_producto = models.CharField('Producto', max_length=60, unique=True)