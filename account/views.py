from django.contrib.auth.views import LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DeleteView

from account.forms import RegisterForm

# Create your views here.
from core.models import Address


class Logout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('core:home')


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('account:login')
    success_message = 'حساب کاربری با موفقیت ایجاد شد، لطفا وارد شوید.'


def profile_view(request):
    return render(request, 'registration/profile.html')


class AddressCreateView(SuccessMessageMixin, CreateView):
    model = Address
    fields = '__all__'
    success_url = reverse_lazy('account:profile')
    template_name = 'registration/address_create_update.html'
    success_message = 'آدرس با موفقیت ایجاد شد.'

    def form_valid(self, form):
        address = form.save(commit=False)
        address.user = self.request.user
        address.save()
        return super().form_valid(form)


class AddressUpdateView(SuccessMessageMixin, UpdateView):
    model = Address
    fields = '__all__'
    success_url = reverse_lazy('account:profile')
    template_name = 'registration/address_create_update.html'
    success_message = 'آدرس با موفقیت ویرایش شد.'

    def form_valid(self, form):
        address = form.save(commit=False)
        address.user = self.request.user
        address.save()
        return super().form_valid(form)


class AddressDeleteView(SuccessMessageMixin, DeleteView):
    model = Address
    template_name = 'registration/address_delete.html'
    success_url = reverse_lazy('account:profile')
    success_message = 'آدرس حذف شد.'
