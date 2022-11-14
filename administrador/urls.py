"""innotekmobil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LoginView, LogoutView
from re import template
from django.contrib import admin
from django.urls import path, include
from administrador.views import *
from administrador import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
# from administrador.views import SignUpView, ProfileUpate
from django.contrib.auth import views as auth_views

from .views import *


urlpatterns = [
    path('', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logoutView/', LogoutView.as_view(template_name='accounts/login.html'), name="logout"),
    path('register/', views.register, name='register'),
    path('index/',index, name='index'),
    path('admin/', admin.site.urls),
    path('perfil/', perfil),
    path('editarperfil/', editperfil),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('help/', ayuda),
    path('contacto/',contacto, name='index'),

# API
    path('v1/conductor', Conductor_APIView.as_view()), 
    path('v1/conductor/<int:pk>/', Conductor_APIView_Detail.as_view()),
    path('v1/ruta', Ruta_APIView.as_view()), 
    path('v1/ruta/<int:pk>/', Ruta_APIView_Detail.as_view()),
    path('v1/paradero', Paradero_APIView.as_view()), 
    path('v1/paradero/<int:pk>/', Paradero_APIView_Detail.as_view()),
      

# DASHBOARD
    path('rutas_7/',rutas_7, name='rutas_7'),
    path('dashboard/',dashboard, name='dashboard'),
    path('dashboard2/',dashboard2, name='dashboard2'),
    path('valla/',valla, name='valla'),
    path('anuncios/',anuncios, name='anuncios'),



 # ADJUNTAR ARCHIVOS
    path('adjuntar_archivos/', ListadoAdjuntar.as_view(template_name = "adjuntar_archivos/formularioadjuntar.html"), name='leer1'),
    path('adjuntar_archivos/detalle/<int:pk>', AdjuntarDetalle.as_view(template_name = "adjuntar_archivos/detalle.html"), name='detalles'),
    path('adjuntar_archivos/crear', AdjuntarCrear.as_view(template_name = "adjuntar_archivos/crear.html"), name='crear'),
    path('adjuntar_archivos/editar/<int:pk>', AdjuntarActualizar.as_view(template_name = "adjuntar_archivos/actualizar.html"), name='actualizar'),
    path('adjuntar_archivos/eliminar/<int:pk>', AdjuntarEliminar.as_view(), name='adjuntar_archivos/eliminar.html'),

    # CARGAR DOCUMENTO
    path('cargar_documento/', ListadoCargar.as_view(template_name = "cargar_documento/formulariocargar.html"), name='leer2'),
    path('cargar_documento/detalle/<int:pk>', CargarDetalle.as_view(template_name = "cargar_documento/detalle.html"), name='detalles'),
    path('cargar_documento/crear', CargarCrear.as_view(template_name = "cargar_documento/crear.html"), name='crear'),
    path('cargar_documento/editar/<int:pk>', CargarActualizar.as_view(template_name = "cargar_documento/actualizar.html"), name='actualizar'), 
    path('cargar_documento/eliminar/<int:pk>', CargarEliminar.as_view(), name='cargar_documento/eliminar.html'),
    
    # CONDUCTOR
    path('conductor/', ListadoConductor.as_view(template_name = "conductor/formularioconductor.html"), name='leer3'),
    path('conductor/detalle/<int:pk>', ConductorDetalle.as_view(template_name = "conductor/detalle.html"), name='detalles'),
    path('conductor/crear', ConductorCrear.as_view(template_name = "conductor/crear.html"), name='crear'),
    path('conductor/editar/<int:pk>', ConductorActualizar.as_view(template_name = "conductor/actualizar.html"), name='actualizar'), 
    path('conductor/eliminar/<int:pk>', ConductorEliminar.as_view(), name='conductor/eliminar.html'),

    # DEPARTAMENTO
    path('departamento/', ListadoDepartamento.as_view(template_name = "departamento/formulariodepartamento.html"), name='leer4'),
    path('departamento/detalle/<int:pk>', DepartamentoDetalle.as_view(template_name = "departamento/detalle.html"), name='detalles'),
    path('departamento/crear', DepartamentoCrear.as_view(template_name = "departamento/crear.html"), name='crear'),
    path('departamento/editar/<int:pk>', DepartamentoActualizar.as_view(template_name = "departamento/actualizar.html"), name='actualizar'), 
    path('departamento/eliminar/<int:pk>', DepartamentoEliminar.as_view(), name='departamento/eliminar.html'),
    
    # MUNICIPIO
    path('municipio/', ListadoMunicipio.as_view(template_name = "municipio/formulariomunicipio.html"), name='leer5'),
    path('municipio/detalle/<int:pk>', MunicipioDetalle.as_view(template_name = "municipio/detalle.html"), name='detalles'),
    path('municipio/crear', MunicipioCrear.as_view(template_name = "municipio/crear.html"), name='crear'),
    path('municipio/editar/<int:pk>', MunicipioActualizar.as_view(template_name = "municipio/actualizar.html"), name='actualizar'), 
    path('municipio/eliminar/<int:pk>', MunicipioEliminar.as_view(), name='municipio/eliminar.html'),
    
    # PARADERO
    path('paradero/', ListadoParadero.as_view(template_name = "paradero/formularioparadero.html"), name='leer6'),
    path('paradero/detalle/<int:pk>', ParaderoDetalle.as_view(template_name = "paradero/detalle.html"), name='detalles'),
    path('paradero/crear', ParaderoCrear.as_view(template_name = "paradero/crear.html"), name='crear'),
    path('paradero/editar/<int:pk>', ParaderoActualizar.as_view(template_name = "paradero/actualizar.html"), name='actualizar'), 
    path('paradero/eliminar/<int:pk>', ParaderoEliminar.as_view(), name='paradero/eliminar.html'),

    # PLAN DE RODAMIENTO
    path('plan_rodamiento/', ListadoPlanRodamiento.as_view(template_name = "plan_rodamiento/formulariorodamiento.html"), name='leer7'),
    path('plan_rodamiento/detalle/<int:pk>', PlanRodamientoDetalle.as_view(template_name = "plan_rodamiento/detalle.html"), name='detalles'),
    path('plan_rodamiento/crear', PlanRodamientoCrear.as_view(template_name = "plan_rodamiento/crear.html"), name='crear'),
    path('plan_rodamiento/editar/<int:pk>', PlanRodamientoActualizar.as_view(template_name = "plan_rodamiento/actualizar.html"), name='actualizar'), 
    path('plan_rodamiento/eliminar/<int:pk>', PlanRodamientoEliminar.as_view(), name='plan_rodamiento/eliminar.html'),

    # RUTA
    path('ruta/', ListadoRuta.as_view(template_name = "ruta/formularioruta.html"), name='leer8'),
    path('ruta/detalle/<int:pk>', RutaDetalle.as_view(template_name = "ruta/detalle.html"), name='detalles'),  
    path('ruta/crear', RutaCrear.as_view(template_name = "ruta/crear.html"), name='crear'),
    path('ruta/editar/<int:pk>', RutaActualizar.as_view(template_name = "ruta/actualizar.html"), name='actualizar'), 
    path('ruta/eliminar/<int:pk>', RutaEliminar.as_view(), name='ruta/eliminar.html'),

    # SUBIR ARCHIVOS
    path('subir_archivos/', ListadoSubirArchivos.as_view(template_name = "subir_archivos/formulariosubir.html"), name='leer9'),
    path('subir_archivos/detalle/<int:pk>', SubirArchivosDetalle.as_view(template_name = "subir_archivos/detalle.html"), name='detalles'),
    path('subir_archivos/crear', SubirArchivosCrear.as_view(template_name = "subir_archivos/crear.html"), name='crear'),
    path('subir_archivos/editar/<int:pk>', SubirArchivosActualizar.as_view(template_name = "subir_archivos/actualizar.html"), name='actualizar'),
    path('subir_archivos/eliminar/<int:pk>', SubirArchivosEliminar.as_view(), name='subir_archivos/eliminar.html'),

    # TURNO
    path('turno/', ListadoTurno.as_view(template_name = "turno/formularioturno.html"), name='leer10'),
    path('turno/detalle/<int:pk>', TurnoDetalle.as_view(template_name = "turno/detalle.html"), name='detalles'),
    path('turno/crear', TurnoCrear.as_view(template_name = "turno/crear.html"), name='crear'),
    path('turno/editar/<int:pk>', TurnoActualizar.as_view(template_name = "turno/actualizar.html"), name='actualizar'), 
    path('turno/eliminar/<int:pk>', TurnoEliminar.as_view(), name='turno/eliminar.html'),  

    # UBICACIÓN
    path('ubicacion/', ListadoUbicacion.as_view(template_name = "ubicacion/formularioubicacion.html"), name='leer11'),
    path('ubicacion/detalle/<int:pk>', UbicacionDetalle.as_view(template_name = "ubicacion/detalle.html"), name='detalles'),
    path('ubicacion/crear', UbicacionCrear.as_view(template_name = "ubicacion/crear.html"), name='crear'),
    path('ubicacion/editar/<int:pk>', UbicacionActualizar.as_view(template_name = "ubicacion/actualizar.html"), name='actualizar'), 
    path('ubicacion/eliminar/<int:pk>', UbicacionEliminar.as_view(), name='ubicacion/eliminar.html'), 
    
    # VEHÍCULO
    path('vehiculo/', ListadoVehiculo.as_view(template_name = "vehiculo/formulariovehiculo.html"), name='leer12'),
    path('vehiculo/detalle/<int:pk>', VehiculoDetalle.as_view(template_name = "vehiculo/detalle.html"), name='detalles'),
    path('vehiculo/crear', VehiculoCrear.as_view(template_name = "vehiculo/crear.html"), name='crear'),
    path('vehiculo/editar/<int:pk>', VehiculoActualizar.as_view(template_name = "vehiculo/actualizar.html"), name='actualizar'), 
    path('vehiculo/eliminar/<int:pk>', VehiculoEliminar.as_view(), name='vehiculo/eliminar.html'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+= static(settings.MEDIA_URL,documen_root=settings.MEDIA_ROOT)
    