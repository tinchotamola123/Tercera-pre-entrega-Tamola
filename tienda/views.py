from django.shortcuts import render , redirect , get_object_or_404
from .models import Prodcto
from .forms import ContactoForm , ProductoForm ,MarcaForm

# Create your views here.

def home(request):
    productos = Prodcto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'tienda/home.html' , data)

def contacto(request):
    data = {
        'form' : ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Enviado a la base"
        else:
            data['form'] = formulario
        
    return render(request, 'tienda/contacto.html' , data)

def galeria(request):
    return render(request, 'tienda/galeria.html')

def agregar_producto(request):
    data = {
        'form' : ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto Agregado Correctamente"
        else:
            data['form'] = formulario
    return render(request, 'producto/agregar.html', data)

def listar_productos(request):
    productos = Prodcto.objects.all()
    data = {
        'productos' : productos
    }
    
    return render(request, 'producto/listar.html', data)

def modificar_producto(request, id):
    
    producto = get_object_or_404(Prodcto, id=id)
    
    data = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario
        
    return render(request, 'producto/modificar.html', data)

def eliminar_producto(request):
    prducto = get_object_or_404(Prodcto, id=id)
    prducto.delete()
    return redirect(to="listar_productos")

def agregar_marca(request):
    data = {
        'form' : MarcaForm()
    }
    
    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Marca Agregada Correctamente"
        else:
            data['form'] = formulario
    return render(request, 'marca/agregar.html', data)

def buscar_producto(request , marca):
    productos = Prodcto.objects.filter(marca=marca).values()
    data = {
        'productos' : productos
    }
    
    return render(request, 'marca/buscar.html', data)
    