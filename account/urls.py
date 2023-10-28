from django.urls import path
from .views import Logout, RegisterView, profile_view, AddressCreateView, AddressUpdateView

app_name = 'account'
urlpatterns = [
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
    path('profile/address/create', AddressCreateView.as_view(), name='profile-address-create'),
    path('profile/address/update/<int:pk>', AddressUpdateView.as_view(), name='profile-address-update'),
]
