from django.urls import path
from .views import admin_home_view, AdminProductListView

app_name = 'product'
urlpatterns = [
    path('panel/', admin_home_view, name='admin-home'),
    path('panel/products/', AdminProductListView.as_view(), name='admin-product-list'),
]
