from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from core.cart import Cart
from product.models import Product


def home_view(request):
    products = Product.objects.filter(is_active=True)

    context = {
        'products': products
    }
    return render(request, 'core/home.html', context)


def cart_view(request):
    cart = Cart(request)

    context = {
        'cart': cart
    }
    return render(request, 'core/cart.html', context)


class ProductDetailView(DetailView):
    queryset = Product.objects.filter(is_active=True)
    template_name = 'core/product_detail.html'
