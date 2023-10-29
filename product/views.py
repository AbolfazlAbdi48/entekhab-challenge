from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from core.models import Order
from product.models import Product


@user_passes_test(lambda u: u.is_superuser)
def admin_home_view(request):
    user_count = User.objects.count()
    product_count = Product.objects.count()
    order_count = Order.objects.count()

    context = {
        'user_count': user_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'product/admin/admin_home.html', context)


class AdminProductListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Product
    template_name = 'product/admin/admin_product_list.html'
    paginate_by = 20

    def test_func(self):
        return self.request.user.is_superuser


class AdminProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    template_name = 'product/admin/admin_product_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy('product:admin-product-list')

    def test_func(self):
        return self.request.user.is_superuser


class AdminProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'product/admin/admin_product_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy('product:admin-product-list')

    def test_func(self):
        return self.request.user.is_superuser


class AdminProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'product/admin/admin_product_delete.html'
    success_url = reverse_lazy('product:admin-product-list')

    def test_func(self):
        return self.request.user.is_superuser


class AdminOrdersListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Order
    template_name = 'product/admin/orders_list.html'
    paginate_by = 20

    def test_func(self):
        return self.request.user.is_superuser


class AdminOrderDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Order
    template_name = 'product/admin/order_detail.html'

    def test_func(self):
        return self.request.user.is_superuser


class AdminUserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'product/admin/admin_user_list.html'
    paginate_by = 20

    def test_func(self):
        return self.request.user.is_superuser
