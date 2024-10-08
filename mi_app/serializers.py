from rest_framework import serializers
from .models import OpcionesMenu, Usuario

class OpcionesMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpcionesMenu
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'rol']
