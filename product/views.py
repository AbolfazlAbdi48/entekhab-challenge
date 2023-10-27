from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from core.models import Order
from product.models import Product


def admin_home_view(request):
    return render(request, 'product/admin/admin_home.html')


class AdminProductListView(ListView):
    model = Product
    template_name = 'product/admin/admin_product_list.html'
    paginate_by = 20


class AdminProductCreateView(CreateView):
    model = Product
    template_name = 'product/admin/admin_product_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy('product:admin-product-list')


class AdminProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/admin/admin_product_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy('product:admin-product-list')


class AdminProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/admin/admin_product_delete.html'
    success_url = reverse_lazy('product:admin-product-list')


class AdminOrdersListView(ListView):
    model = Order
    template_name = 'product/admin/orders_list.html'
    paginate_by = 20


class AdminOrderDetailView(DetailView):
    model = Order
    template_name = 'product/admin/order_detail.html'
