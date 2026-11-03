from django.shortcuts import render, get_object_or_404
from myShop.models import Product, SerialNumber, ProductComment

def product_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all().order_by('-id')
    return render(request, 'product_list.html', {'products': products})

def product_detail_view(request, id):
    if request.method == 'GET':
        product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

# Create your views here.
