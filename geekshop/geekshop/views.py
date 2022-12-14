from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product
from django.views.decorators.cache import never_cache

@never_cache
def index(request):
    title = 'GeekShop'
    products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')[:4]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/contacts.html', context)