import json
from django.shortcuts import render


def json_to_context(path):
    with open(path, encoding='utf-8') as json_file:
        return json.load(json_file)


def index(request):
    context = json_to_context('mainapp/fixtures/index_context.json')
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = json_to_context('mainapp/fixtures/products_context.json')
    return render(request, 'mainapp/products.html', context)
