from django.contrib import admin
from administrador.models import AdjuntarArchivos  
from administrador.models import CargarDocumento
from administrador.models import Conductor
from administrador.models import Departamento
from administrador.models import Municipio
from administrador.models import Paradero
from administrador.models import PlanRodamiento
from administrador.models import Ruta
from administrador.models import SubirArchivos
from administrador.models import Turno
from administrador.models import Ubicacion
from administrador.models import Vehiculo
# Register your models here.
admin.site.register(AdjuntarArchivos)
admin.site.register(CargarDocumento)
admin.site.register(Conductor)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Paradero)
admin.site.register(PlanRodamiento)
admin.site.register(Ruta)
admin.site.register(SubirArchivos)
admin.site.register(Turno)
admin.site.register(Ubicacion)
admin.site.register(Vehiculo)