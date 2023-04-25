from django import forms
from .models import Contacto , Prodcto , Marca


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