
from django.shortcuts import render
from .models import Producte, Categoria

def product_list(request, category_id=None):
    if category_id:
        products = Producte.objects.filter(categoria__id=category_id)
    else:
        products = Producte.objects.all()
    categories = Categoria.objects.all()
    return render(request, 'product_list.html', {'products': products, 'categories': categories, 'category_id': category_id})