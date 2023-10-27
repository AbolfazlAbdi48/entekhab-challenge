from django.urls import path
from .views import admin_home_view

app_name = 'product'
urlpatterns = [
    path('panel/', admin_home_view, name='admin-home'),
]
