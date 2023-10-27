from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

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
