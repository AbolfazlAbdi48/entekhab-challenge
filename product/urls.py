from django.urls import path
from .views import (
    admin_home_view,
    AdminProductListView,
    AdminProductCreateView,
    AdminProductUpdateView,
    AdminProductDeleteView,
    AdminOrdersListView
)

app_name = 'product'
urlpatterns = [
    path('panel/', admin_home_view, name='admin-home'),
    path('panel/products/', AdminProductListView.as_view(), name='admin-product-list'),
    path('panel/orders/', AdminOrdersListView.as_view(), name='admin-order-list'),
    path('panel/products/create', AdminProductCreateView.as_view(), name='admin-product-create'),
    path('panel/products/update/<int:pk>', AdminProductUpdateView.as_view(), name='admin-product-update'),
    path('panel/products/delete/<int:pk>', AdminProductDeleteView.as_view(), name='admin-product-delete'),
]
