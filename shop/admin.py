from django.contrib import admin
from .models import Categoria, Tag, Producte, Cistella, Compra, DetallCompra

# Inline classes
class CategoriaInline(admin.TabularInline):
    model = Categoria
    extra = 1
    readonly_fields = ["descripcio"]

class DetallCompraInline(admin.TabularInline):
    model = DetallCompra
    extra = 1
    readonly_fields = ["producte", "quantitat", "preu_unitari"]

class ProducteInline(admin.TabularInline):
    model = Producte
    extra = 1
    readonly_fields = ["descripcio"]

# Admin classes
class CategoriaAdmin(admin.ModelAdmin):
    inlines = [CategoriaInline, ProducteInline]
    list_display = ['nom','parent']

class CistellaAdmin(admin.ModelAdmin):
    list_display = ['usuari', 'quantitat']
    filter_horizontal = ('producte',)

class CompraAdmin(admin.ModelAdmin):
    inlines = [DetallCompraInline]
    list_display = ['usuari', 'data_compra', 'preu_total']

# Register models
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Cistella, CistellaAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(DetallCompra)
admin.site.register(Producte)
admin.site.register(Tag)