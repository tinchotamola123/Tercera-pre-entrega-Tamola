from django.contrib import admin
from tienda import models
# Register your models here.

admin.site.register(models.Marca)
admin.site.register(models.Prodcto)
admin.site.register(models.Contacto)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'precio', 'nuevo', 'marca"')
    
