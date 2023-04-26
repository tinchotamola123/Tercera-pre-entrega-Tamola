from django.shortcuts import render , redirect , get_object_or_404
from .models import Prodcto , Marca
from .forms import ContactoForm , ProductoForm ,MarcaForm
from django.contrib import messages

# Create your views here.
""""
Vistas Home
"""
def home(request):
    productos = Prodcto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'tienda/home.html' , data)

""""
Vistas Contacto

"""
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

""""
Vistas Productos

"""

def agregar_producto(request):
    data = {
        'form' : ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Agregado Correcatmente")
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
            messages.success(request, "Editado Correcatmente")
            return redirect(to="listar_productos")
        data["form"] = formulario
        
    return render(request, 'producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Prodcto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correcatmente")
    return redirect(to="listar_productos")

def buscar_producto(request , producto):
    productos = Prodcto.objects.filter(producto=producto).values()
    data = {
        'productos' : productos
    }
    
    return render(request, 'producto/buscar.html', data)

""""
Vistas Marcas

"""

def agregar_marca(request):
    data = {
        'form' : MarcaForm()
    }
    
    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Marca Agregada Correcatmente")
        else:
            data['form'] = formulario
    return render(request, 'marca/agregar.html', data)

    
def listar_marcas(request):
    marcas = Marca.objects.all()
    data = {
        'marcas' : marcas
    }
    
    return render(request, 'marca/listar.html', data)

def modificar_marca(request, id):
    
    marca = get_object_or_404(Marca, id=id)
    
    data = {
        'form': MarcaForm(instance=marca)
    }
    
    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST, instance=marca)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado Correcatmente")
            return redirect(to="listar_marcas")
        data["form"] = formulario
        
    return render(request, 'marca/modificar.html', data)

def eliminar_marca(request, id):
    marca = get_object_or_404(Marca, id=id)
    marca.delete()
    messages.success(request, "Eliminado Correcatmente")
    return redirect(to="listar_marcas")