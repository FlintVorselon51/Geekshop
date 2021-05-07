from django.shortcuts import render

from .models import ProductCategory, Product


def index(request):
    context = {'title': 'Geekshop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
