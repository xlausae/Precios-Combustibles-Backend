from django.contrib       import admin
from .models.departamentos   import Departamentos
from .models.banderas     import Banderas
from .models.municipios import Municipios
from .models.estaciones_productos   import Estaciones_productos
from .models.tipo_productos import Tipo_productos
from .models.estaciones      import Estaciones

admin.site.register(Departamentos)
admin.site.register(Banderas)
admin.site.register(Municipios)
admin.site.register(Estaciones_productos)
admin.site.register(Tipo_productos)
admin.site.register(Estaciones)

