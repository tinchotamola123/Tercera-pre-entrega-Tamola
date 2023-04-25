from django.contrib import admin
from tienda import models
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre" , "precio", "nuevo", "marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca","nuevo"]
    list_per_page = 5

admin.site.register(models.Marca)
admin.site.register(models.Prodcto)
admin.site.register(models.Contacto)