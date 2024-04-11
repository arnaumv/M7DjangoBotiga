# urls.py


from django.urls import path
from . import views
from .api import product_list

urlpatterns = [
    path('shop/', views.product_list, name='product_list'),
    #path('shop/products/category/<int:category_id>/', views.product_list, name='product_list_by_category'),

    path('products/', product_list, name='product_list'),
    path('products/<int:category_id>/', product_list, name='product_list_by_category'),
    path('cart/', views.cart, name='cart'),
]