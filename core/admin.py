from django.contrib import admin
from .models import Address, Order, OrderDetail

# Register your models here.
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderDetail)
