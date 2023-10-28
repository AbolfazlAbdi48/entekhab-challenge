import json

from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, get_object_or_404

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


def cart_add_ajax_view(request, product_id):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            cd = data.get('payload')  # cleaned daya
            count = cd.get('count')
            # check count greater than 1
            if int(count) < 1:
                count = 1

            cart = Cart(request)
            product = get_object_or_404(Product, id=product_id, is_active=True)

            # check for product stock
            if int(count) <= product.stock:
                cart.add(product, count=int(count), override_count=True)
                return JsonResponse({'status': 'added'})
            return JsonResponse({'status': 'failed'})

        return JsonResponse({'status': 'Invalid request'}, status=400)
    return HttpResponseBadRequest('Invalid request')


def cart_remove_ajax_view(request, product_id):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'DELETE':
            cart = Cart(request)
            product = get_object_or_404(Product, id=product_id, is_active=True)

            cart.remove(product)
            return JsonResponse({'status': 'deleted', 'total_price': cart.get_total_price()})

        return JsonResponse({'status': 'Invalid request'}, status=400)
    return HttpResponseBadRequest('Invalid request')


class ProductDetailView(DetailView):
    queryset = Product.objects.filter(is_active=True)
    template_name = 'core/product_detail.html'
