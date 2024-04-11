from django.http import JsonResponse
from .models import Producte, Categoria
from django.core import serializers

def product_list(request, category_id=None):
    if category_id:
        products = Producte.objects.filter(categoria__id=category_id)
    else:
        products = Producte.objects.all()
    categories = Categoria.objects.all()

    products_json = serializers.serialize('json', products)
    categories_json = serializers.serialize('json', categories)

    return JsonResponse({'products': products_json, 'categories': categories_json, 'category_id': category_id})