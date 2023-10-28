from django.urls import path
from .views import Logout, RegisterView, profile_view

app_name = 'account'
urlpatterns = [
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
]
