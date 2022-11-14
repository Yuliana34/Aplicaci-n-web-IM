from rest_framework import serializers
from administrador.models import Conductor,Paradero, Ruta

class ConductorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Conductor 
        fields = "__all__" 


class RutaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = "__all__" 

class ParaderoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Paradero
        fields = "__all__" 