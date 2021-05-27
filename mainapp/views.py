from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import ProductCategory, Product


def index(request):
    context = {'title': 'Geekshop'}
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None, page=1):
    context = {
        'title': 'Каталог',
        'categories': ProductCategory.objects.all(),
    }
    product_list = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(product_list, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context |= {'products': products_paginator}
    return render(request, 'mainapp/products.html', context)
