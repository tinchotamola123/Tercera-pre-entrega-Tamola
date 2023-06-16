from rest_framework import viewsets , permissions
from tienda.models import Prodcto , Contacto , Marca
from API.serializers import ProdctoSerializer , MarcaSerializer , ContactoSerializer
from django.shortcuts import render

# Create your views here.

class ProdctoViewSet(viewsets.ModelViewSet):
    queryset = Prodcto.objects.all()
    serializer_class = ProdctoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]