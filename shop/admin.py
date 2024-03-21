from django.contrib import admin
from .models import Categoria, Tag, Producte, Cistella, Compra, DetallCompra

admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(Producte)
admin.site.register(Cistella)
admin.site.register(Compra)
admin.site.register(DetallCompra)