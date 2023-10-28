from django.contrib.auth.views import LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.views.generic import CreateView

from account.forms import RegisterForm


# Create your views here.


class Logout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('core:home')


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('account:login')
    success_message = 'حساب کاربری با موفقیت ایجاد شد، لطفا وارد شوید.'
