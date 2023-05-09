from django import forms
from .models import Contacto , Prodcto , Marca
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidaor
from django.forms import ValidationError


class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        #fields = ["nombre" , "correo" , "ripo_consulta" , "mensaje" , "avisos"]
        fields = '__all__'
        
        
class ProductoForm(forms.ModelForm):
    
    nombre = forms.CharField(max_length=50, min_length=3)
    precio = forms.IntegerField(max_value=1000000,min_value=1)
    imagen = forms.ImageField(validators=[MaxSizeFileValidaor(max_file_size=2)])
    
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]    
        existe = Prodcto.objects.filter(nombre__iexact=nombre).exists()
        
        if existe:
            raise ValidationError("Este nombre ya existe.")
        
        return nombre
    
    class Meta:
        model = Prodcto
        fields = '__all__'
        
        widgets = {
            "fecha_fabricacion": forms.SelectDateWidget()
        }
        
class MarcaForm(forms.ModelForm):
    
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]    
        existe = Marca.objects.filter(nombre__iexact=nombre).exists()
        
        if existe:
            raise ValidationError("Esta marca ya existe.")

        return nombre
    class Meta:
        model = Marca
        fields = '__all__'
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]
        exclude = ()
        # Saca los mensajes de ayuda
        help_texts = {
            'username': None,
            'first_name': None,
            'last_name': None,
            'email': None,
            'password1' : None,
            'password2' : None
        }