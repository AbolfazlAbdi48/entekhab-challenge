from django.urls import path
from .views import home_view, ProductDetailView

app_name = 'core'
urlpatterns = [
    path('', home_view, name='home'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
]
