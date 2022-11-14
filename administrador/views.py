from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from administrador.forms import *
#from cuentas.forms import Userform
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

#API
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import ConductorSerializers, RutaSerializers, ParaderoSerializers
from .models import Conductor, Ruta, Paradero


# PERFIL DE USUARIO
from django.contrib.auth.models import User


#PRUEBA
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
UserModel = get_user_model()
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegisterUserForm

def register(request):
    if request.user.is_authenticated:
        print('Ya autenticado')
        return HttpResponseRedirect(reverse('register'))
    else:
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            # RegisterUserForm se crea a partir del modelo de usuario, todas las restricciones de campo del modelo se verifican para considerarlo un formulario válido
            if form.is_valid():
                print('formulario valido')
                # Guardar usuario en la base de datos pero con is_active = False
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                # Redirigir al usuario para iniciar sesión
                messages.success(request, 'Registrado Correctamente')
                return HttpResponseRedirect(reverse('login'))
            else:
                #print('Invalid form: %s' % form.errors.as_data())
                #print(type(form.errors.as_data()))
                if form.errors:
                    #messages.info(request, 'Input field errors:')
                    for key, values in form.errors.as_data().items():
                        #print("Bad value: %s - %s" % (key, values))
                        if key == 'username':
                            messages.info(request, 'Campos de entrada de errores')
                            break
                        else:
                            for error_value in values:
                                print(error_value)
                                #print(type(error_value))
                                messages.info(request, '%s' % (error_value.message))
                return HttpResponseRedirect(reverse('register'))
        else:
            form = RegisterUserForm()

            context = {
                'form': form
            }
            return render(request, 'usersAuth/register.html', context)

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # Redirect user to login
        messages.success(request, 'Confirmación exitosa por correo electrónico, puede proceder a iniciar sesión.')
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponse('¡El enlace de activación no es válido!')

#LOGIN
def login(request):
    return redirect (request, "/")

# PERFIL
def perfil(request):
    return render(request, "perfil.html")

# PERFIL
def editperfil(request):
    return render(request, "editperfil.html")

# CONFIRMACIÓN
def confirmar(request):
    return render(request, "accounts/confirm_email.html")

# CAMPANARIO
def rutas_7(request):
    return render(request, "dashboard/rutas_7.html")

# PANTALLA 1_CAMPANARIO
def dashboard(request):
    return render(request, "dashboard/dash.html")

# PANTALLA 2_CAMPANARIO
def dashboard2(request):
 return render(request, "dashboard/dash2.html")
    
# VALLA
def valla(request):
 return render(request, "dashboard/valla.html")

 # VALLA
def anuncios(request):
 return render(request, "dashboard/anuncios.html")

# INDEX
def index(request):
    return render (request, "index.html")


def gestor(request):
    return render (request, "templates/gestor/dash.html")

# AYUDA
def ayuda(request):
    return render(request, "help.html")


# RECUPERACIÓN DE CONTRASEÑA
def recuperar(request):
    return render (request, "accounts/password_reset.html")

# LOGICA DEL REGISTRO
def atenticacionregistro (request):
    return render (request, "accounts/signup.html")

#CONFIRMACION
def verificacion (request):
    return render (request, "accounts/verification_sent.html")

# CONTACTAR
def contacto (request):
    if request.method=="POST":
        subject=request.POST["asunto"]
        message=request.POST["mensaje"] + " " + request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["dayktamayo1@misena.edu.co"]
        send_mail(subject,message,email_from,recipient_list)
        return HttpResponseRedirect(reverse('index'))
    messages.success(request, 'Mensaje enviado con éxito')
    return render(request, "index.html")
            
# ADJUNTAR ARCHIVOS
class ListadoAdjuntar(ListView):
    template_name = '/templates/adjuntar_archivos/formularioadjuntar.html'
    model = AdjuntarArchivos
    paginate_by = 10
    context_object_name = 'object_list'
    
class AdjuntarCrear(SuccessMessageMixin, CreateView):
    model = AdjuntarArchivos
    form = AdjuntarArchivos
    fields = "__all__"
    success_message ='Archivo adjunto creado correctamente'
    def get_success_url(self):        
        return reverse('leer1')

class AdjuntarDetalle (DetailView):
    model = AdjuntarArchivos

class AdjuntarActualizar(SuccessMessageMixin,UpdateView):
    model = AdjuntarArchivos
    form = AdjuntarArchivos
    fields = "__all__"
    success_message = '¡Archivo adjunto actualizado correctamente!'
    def get_success_url(self):               
        return reverse('leer1')

class AdjuntarEliminar(SuccessMessageMixin, DeleteView): 
    model = AdjuntarArchivos
    form = AdjuntarArchivos
    fields = "__all__"
    def get_success_url(self): 
        success_message = '¡Archivo adjunto eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer1')

# CARGAR DOCUMENTO
class ListadoCargar(ListView):
    template_name = '/templates/cargar_documento/formulariocargar.html'
    model = CargarDocumento
    paginate_by = 10
    context_object_name = 'object_list'
    
class CargarCrear(SuccessMessageMixin, CreateView):
    model = CargarDocumento
    form = CargarDocumento
    fields = "__all__"
    success_message ='Documento cargado creado correctamente'
    def get_success_url(self):        
        return reverse('leer2') 

class CargarDetalle (DetailView):
    model = CargarDocumento

class CargarActualizar(SuccessMessageMixin,UpdateView):
    model = CargarDocumento
    form = CargarDocumento
    fields = "__all__"  
    success_message = '¡Documento cargado actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer2') 

class CargarEliminar(SuccessMessageMixin, DeleteView): 
    model = CargarDocumento
    form = CargarDocumento
    fields = "__all__"     
    def get_success_url(self): 
        success_message = '¡Documento cargado eliminado correctamente !'
        messages.success (self.request, (success_message))       
        return reverse('leer2')

# CONDUCTOR
class ListadoConductor(ListView):
    template_name = '/templates/conductor/formularioconductor.html'
    model = Conductor
    paginate_by = 10
    context_object_name = 'object_list'

class ConductorCrear(SuccessMessageMixin, CreateView):
    model = Conductor
    form = Conductor
    fields = "__all__"
    success_message ='Conductor creado correctamente'
    def get_success_url(self):        
        return reverse('leer3')

class ConductorDetalle (DetailView):
    model = Conductor

class ConductorActualizar(SuccessMessageMixin,UpdateView):
    model = Conductor
    form = Conductor
    fields = "__all__"
    success_message = '¡Conductor actualizado correctamente!'
    def get_success_url(self):               
        return reverse('leer3')

class ConductorEliminar(SuccessMessageMixin, DeleteView): 
    model = Conductor
    form = Conductor
    fields = "__all__"     
    def get_success_url(self): 
        success_message = '¡Conductor eliminado correctamente!' 
        messages.success (self.request, (success_message))       
        return reverse('leer3') 
 
# DEPARTAMENTO
class ListadoDepartamento(ListView):
    template_name = '/templates/departamento/formulariodepartamento.html'
    model = Departamento
    paginate_by = 10
    context_object_name = 'object_list'
    
class DepartamentoCrear(SuccessMessageMixin, CreateView):
    model = Departamento
    form =  Departamento
    fields = "__all__"
    success_message ='Departamento creado correctamente'
    def get_success_url(self):        
        return reverse('leer4') 

class DepartamentoDetalle (DetailView):
    model = Departamento

class DepartamentoActualizar(SuccessMessageMixin,UpdateView):
    model = Departamento
    form =  Departamento
    fields = "__all__"  
    success_message = '¡Departamento actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer4') 

class DepartamentoEliminar(SuccessMessageMixin, DeleteView): 
    model = Departamento
    form =  Departamento
    fields = "__all__"     
    def get_success_url(self): 
        success_message = '¡Departamento eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer4')


# MUNICIPIO
class ListadoMunicipio(ListView):
    template_name = '/templates/municipio/formulariomunicipio.html'
    model = Municipio
    paginate_by = 10
    context_object_name = 'object_list'

class MunicipioCrear(SuccessMessageMixin, CreateView):
    model = Municipio
    form =  Municipio
    fields = "__all__"
    success_message ='Municipio creado correctamente'
    def get_success_url(self):        
        return reverse('leer5') 

class MunicipioDetalle (DetailView):
    model = Municipio

class MunicipioActualizar(SuccessMessageMixin,UpdateView):
    model = Municipio
    form =  Municipio
    fields = "__all__"  
    success_message = '¡Municipio actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer5') 

class MunicipioEliminar(SuccessMessageMixin, DeleteView): 
    model = Municipio
    form =  Municipio
    fields = "__all__"     
    def get_success_url(self): 
        success_message = '¡Municipio eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer5')


# PARADERO
class ListadoParadero(ListView):
    template_name = '/templates/paradero/formularioparadero.html'
    model = Paradero
    paginate_by = 10
    context_object_name = 'object_list'

class ParaderoCrear(SuccessMessageMixin, CreateView):
    model = Paradero
    form =  Paradero
    fields = "__all__"
    success_message ='Paradero creado correctamente'
    def get_success_url(self):        
        return reverse('leer6') 

class ParaderoDetalle (DetailView):
    model = Paradero

class ParaderoActualizar(SuccessMessageMixin,UpdateView):
    model = Paradero
    form =  Paradero
    fields = "__all__"  
    success_message = '¡Paradero actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer6') 

class ParaderoEliminar(SuccessMessageMixin, DeleteView): 
    model = Paradero
    form =  Paradero
    fields = "__all__"     
    def get_success_url(self): 
        success_message = '¡Paradero eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer6')


# PLAN DE RODAMIENTO
class ListadoPlanRodamiento(ListView):
    model = PlanRodamiento

class PlanRodamientoCrear(SuccessMessageMixin, CreateView):
    model = PlanRodamiento
    form = PlanRodamiento
    fields = "__all__"
    success_message ='Plan de rodamiento creado correctamente'
    def get_success_url(self):        
        return reverse('leer7') 

class PlanRodamientoDetalle (DetailView):
    model = PlanRodamiento

class PlanRodamientoActualizar(SuccessMessageMixin,UpdateView):
    model = PlanRodamiento
    form = PlanRodamiento
    fields = "__all__"  
    success_message = '¡Plan de rodamiento actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer7') 

class PlanRodamientoEliminar(SuccessMessageMixin, DeleteView): 
    model = PlanRodamiento
    form = PlanRodamiento
    fields = "__all__"     
    def get_success_url(self): 
        success_message = '¡Plan de rodamiento eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer7')


# RUTA
class ListadoRuta(ListView):
    template_name = '/templates/ruta/formularioruta.html'
    model = Ruta
    paginate_by = 10
    context_object_name = 'object_list'
        
class RutaCrear(SuccessMessageMixin, CreateView):
    model = Ruta
    form = Ruta
    fields = "__all__"
    success_message ='Ruta creada correctamente'
    def get_success_url(self):        
        return reverse('leer8') 

class RutaDetalle (DetailView):
    model = Ruta

class  RutaActualizar(SuccessMessageMixin,UpdateView):
    model =  Ruta
    form = Ruta
    fields = "__all__" 
    success_message = 'Ruta actualizada correctamente !' 
    def get_success_url(self):               
        return reverse('leer8')
    
class RutaEliminar(SuccessMessageMixin, DeleteView): 
    model = Ruta 
    form = Ruta
    fields = "__all__"     
    def get_success_url(self): 
        success_message = 'Ruta eliminada correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer8')    


# SUBIR ARCHIVO
class ListadoSubirArchivos(ListView):
    template_name = '/templates/subir_archivos/formulariosubir.html'
    model = SubirArchivos
    paginate_by = 10
    context_object_name = 'object_list'
    
class SubirArchivosCrear(SuccessMessageMixin, CreateView):
    model = SubirArchivos
    form = SubirArchivos
    fields = "__all__"
    success_message ='Archivo creado correctamente'
    def get_success_url(self):        
        return reverse('leer9') 

class SubirArchivosDetalle (DetailView):
    model = SubirArchivos

class SubirArchivosActualizar(SuccessMessageMixin,UpdateView):
    model = SubirArchivos
    form = SubirArchivos
    fields = "__all__" 
    success_message = '¡Archivo subido actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer9') 

class SubirArchivosEliminar(SuccessMessageMixin, DeleteView): 
    model = SubirArchivos 
    form = SubirArchivos
    fields = "__all__"     
    def get_success_url(self): 
        success_message = '¡Archivo subido eliminado correctamente!'  
        messages.success (self.request, (success_message))       
        return reverse('leer9') 


# TURNO
class ListadoTurno(ListView):
    template_name = '/templates/turno/formularioturno.html'
    model = Turno
    paginate_by = 10
    context_object_name = 'object_list'
    
class TurnoCrear(SuccessMessageMixin, CreateView):
    model = Turno
    form = Turno
    fields = "__all__"
    success_message ='Turno creado correctamente'     
    def get_success_url(self):        
        return reverse('leer10') 

class TurnoDetalle (DetailView):
    model = Turno

class TurnoActualizar(SuccessMessageMixin,UpdateView):
    model = Turno
    form = Turno
    fields = "__all__" 
    success_message = 'Turno actualizado correctamente !' 
    def get_success_url(self):               
        return reverse('leer10') 

class TurnoEliminar(SuccessMessageMixin, DeleteView): 
    model = Turno
    form = Turno
    fields = "__all__"     
    def get_success_url(self): 
        success_message = '¡Turno eliminado correctamente !'
        messages.success (self.request, (success_message))       
        return reverse('leer10') 


# UBICACIÓN
class ListadoUbicacion(ListView):
    template_name = '/templates/ubicacion/formularioubicacion.html'
    model = Ubicacion
    paginate_by = 3
    context_object_name = 'object_list'

class UbicacionCrear(SuccessMessageMixin, CreateView):
    model = Ubicacion
    form = Ubicacion
    fields = "__all__"
    success_message ='Ubicación creada correctamente'
    def get_success_url(self):        
        return reverse('leer11') 

class UbicacionDetalle (DetailView):
    model = Ubicacion

class UbicacionActualizar(SuccessMessageMixin,UpdateView):
    model = Ubicacion
    form = Ubicacion
    fields = "__all__"  
    success_message = '¡Ubicación actualizada correctamente!' 
    def get_success_url(self):               
        return reverse('leer11') 

class UbicacionEliminar(SuccessMessageMixin, DeleteView): 
    model = Ubicacion
    form = Ubicacion
    fields = "__all__"     
    def get_success_url(self): 
        success_message = '¡Ubicación eliminada correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer11')


# VEHÍCULO
class ListadoVehiculo(ListView):
    template_name = '/templates/vehiculo/formulariovehiculo.html'
    model = Vehiculo
    paginate_by = 10
    context_object_name = 'object_list'

class VehiculoCrear(SuccessMessageMixin, CreateView):
    model = Vehiculo
    form = Vehiculo
    fields = "__all__"
    success_message ='Vehiculo creado correctamente'
    def get_success_url(self):        
        return reverse('leer12') 

class VehiculoDetalle (DetailView):
    model = Vehiculo

class VehiculoActualizar(SuccessMessageMixin,UpdateView):
    model = Vehiculo
    form = Vehiculo
    fields = "__all__"  
    success_message = '¡Vehiculo actualizado correctamente!' 
    def get_success_url(self):               
        return reverse('leer12') 

class VehiculoEliminar(SuccessMessageMixin, DeleteView): 
    model = Vehiculo
    form = Vehiculo
    fields = "__all__"     
    def get_success_url(self): 
        success_message = '¡Vehiculo eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('leer12')


#API REST CONDUCTOR
class Conductor_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = Conductor.objects.all()
        serializer = ConductorSerializers(post, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ConductorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Conductor_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Conductor.objects.get(pk=pk)
        except Conductor.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = ConductorSerializers(post)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = ConductorSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#API REST RUTA
class Ruta_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = Ruta.objects.all()
        serializer = RutaSerializers(post, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = RutaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Ruta_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Ruta.objects.get(pk=pk)
        except Ruta.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = RutaSerializers(post)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = RutaSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# API REST PARADERO
class Paradero_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = Paradero.objects.all()
        serializer = ParaderoSerializers(post, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ParaderoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class Paradero_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Paradero.objects.get(pk=pk)
        except Paradero.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = ParaderoSerializers(post)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = ParaderoSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    