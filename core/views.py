from django.shortcuts import render

# Create your views here.
from product.models import Product


def home_view(request):
    products = Product.objects.filter(is_active=True)

    context = {
        'products': products
    }
    return render(request, 'core/home.html', context)
