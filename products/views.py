from django.shortcuts import render
from .models import Product


# A view to return the all products and search queries
def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


# A view to return a single product
def product_detail(request, product_id):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/product_detail.html', context)
