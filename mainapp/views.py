from django.shortcuts import render
from django.views.generic.list import ListView

from .models import ProductCategory, Product


def index(request):
    context = {'title': 'Geekshop'}
    return render(request, 'mainapp/index.html', context)


class ProductsView(ListView):
    model = Product
    template_name = 'mainapp/products.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        context |= {
            'title': 'Каталог',
            'categories': ProductCategory.objects.all()
        }
        if category_id:
            context['object_list'] = Product.objects.filter(category_id=category_id)
        print(context)
        return context

# def products(request, category_id=None, page=1):
#     context = {
#         'title': 'Каталог',
#         'categories': ProductCategory.objects.all(),
#     }
#     product_list = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#     paginator = Paginator(product_list, per_page=3)
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#     context |= {'products': products_paginator}
#     return render(request, 'mainapp/products.html', context)
