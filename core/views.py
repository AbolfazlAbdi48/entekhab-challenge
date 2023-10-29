import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import DetailView

from core.cart import Cart
from core.forms import CheckoutForm
from core.models import Address, Order, OrderDetail
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


@login_required
def checkout_view(request):
    cart = Cart(request)
    form = CheckoutForm(request.POST or None)

    if form.is_valid():
        cd = form.cleaned_data  # cleaned data

        # get address
        address = get_object_or_404(Address, user=request.user, id=cd.get('address'))
        # get or create order
        order, created = Order.objects.get_or_create(user=request.user, is_paid=False, address__isnull=True)

        # save order's address & message
        order.address = address
        order.message = cd.get('message')
        order.save()

        # create order details option from cart objects
        order_details = []
        for item in cart:
            order_details.append(
                OrderDetail(
                    order=order,
                    product=item.get('product'),
                    count=item.get('count'),
                    price=item.get('price')
                )
            )
        OrderDetail.objects.bulk_create(order_details)

        messages.success('سفارش شما با موفقیت ثبت شد.')
        return redirect('core:cart-payment', args=[order.id])

    context = {
        'cart': cart,
        'form': form
    }
    return render(request, 'core/checkout.html', context)


def payment_simulation_view(request, order_id):
    try:
        order = Order.objects.get(user=request.user, id=order_id, is_paid=False)
        order.is_paid = True
        order.save()

        # decrease order's products stock
        products = []
        for order_detail in order.order_details.all():
            products.append(order_detail.product)
            order_detail.product.stock -= order_detail.count
        Product.objects.bulk_update(products, ["stock"])

    except Order.DoesNotExist:
        raise Http404

    context = {
        'order': order
    }
    return render(request, 'core/payment_simulation.html', context)


class ProductDetailView(DetailView):
    queryset = Product.objects.filter(is_active=True)
    template_name = 'core/product_detail.html'
