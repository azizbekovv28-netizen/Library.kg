from django.urls import path
from myShop.views import product_list_view, product_detail_view

urlpatterns = [
    path('products/', product_list_view, name='product_list'),
    path('products/<int:id>/', product_detail_view, name='product_detail')
]
