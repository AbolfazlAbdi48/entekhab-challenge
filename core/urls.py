from django.urls import path
from .views import (
    home_view,
    cart_view,
    cart_add_ajax_view,
    cart_remove_ajax_view,
    checkout_view,
    payment_simulation_view,
    ProductDetailView
)

app_name = 'core'
urlpatterns = [
    path('', home_view, name='home'),
    path('cart/', cart_view, name='cart'),
    path('cart/add/<product_id>', cart_add_ajax_view, name='cart-add'),
    path('cart/remove/<product_id>', cart_remove_ajax_view, name='cart-remove'),
    path('cart/checkout/', checkout_view, name='cart-checkout'),
    path('cart/checkout/payment/<int:order_id>', payment_simulation_view, name='cart-payment'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
]
