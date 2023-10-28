from django.urls import path
from .views import (
    home_view,
    cart_view,
    ProductDetailView
)

app_name = 'core'
urlpatterns = [
    path('', home_view, name='home'),
    path('cart/', cart_view, name='cart'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
]
