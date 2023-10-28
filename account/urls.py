from django.urls import path
from .views import Logout, RegisterView

app_name = 'account'
urlpatterns = [
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
