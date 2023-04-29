from django import forms
from .models import Contacto , Prodcto , Marca
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        #fields = ["nombre" , "correo" , "ripo_consulta" , "mensaje" , "avisos"]
        fields = '__all__'
        
        
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Prodcto
        fields = '__all__'
        
        widgets = {
            "fecha_fabricacion": forms.SelectDateWidget()
        }
        
class MarcaForm(forms.ModelForm):
    
    class Meta:
        model = Marca
        fields = '__all__'
        
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]
        exclude = ()