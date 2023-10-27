from django.shortcuts import render


# Create your views here.
def admin_home_view(request):
    return render(request, 'product/admin/admin_home.html')
