# urls.py


from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.product_list, name='product_list'),
    path('shop/products/category/<int:category_id>/', views.product_list, name='product_list_by_category'),
]