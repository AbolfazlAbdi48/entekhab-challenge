from django.urls import path, include
from .views import Logout, RegisterView

app_name = 'account'
urlpatterns = [
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
]
