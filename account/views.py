from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy


# Create your views here.


class Logout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('core:home')
