from django.urls import path, include
from .views import Logout

app_name = 'account'
urlpatterns = [
    path('logout/', Logout.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
]
