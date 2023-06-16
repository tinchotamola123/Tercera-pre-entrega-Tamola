from tienda.models import Prodcto , Contacto , Marca
from rest_framework import serializers

class ProdctoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prodcto
        fields = '__all__'
        
class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'
        
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'