from django.contrib.auth.models import User
from django.db import models
from extensions.utils import generate_order_id
from product.models import Product


# Create your models here.


class Address(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, related_name='addresses', verbose_name='کاربر'
    )
    city = models.CharField(max_length=50, verbose_name='شهر')
    full_address = models.TextField(verbose_name='آدرس کامل')
    zip_code = models.CharField(max_length=20, verbose_name='کد پستی')
    phone_number = models.CharField(max_length=20, verbose_name='شماره تماس')
    name = models.CharField(max_length=50, verbose_name='نام تحویل گیرنده')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین ویرایش')

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = '3. آدرس ها'
        ordering = ('-created',)

    def __str__(self):
        return f"{self.name} | {self.city}"


class Order(models.Model):
    id = models.CharField(
        max_length=255, default=generate_order_id, primary_key=True, editable=False, unique=True
    )
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='orders', verbose_name='کاربر'
    )
    address = models.ForeignKey(
        Address, on_delete=models.PROTECT, null=True, blank=True, verbose_name='آدرس'
    )
    message = models.TextField(null=True, blank=True, verbose_name='پیام')
    is_paid = models.BooleanField(default=False, verbose_name='وضعیت پرداخت')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = '1. سفارشات'
        ordering = ('-created',)

    def total_order_detail_price(self):
        total = 0
        for order_detail in self.order_details.all():
            total += order_detail.total_price()

        return total

    total_order_detail_price.short_description = 'مجموع سبد خرید'

    def __str__(self):
        return f"سفارش : {self.user} - شناسه : {self.id}"


class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_details', verbose_name='سفارش'
    )
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, verbose_name='محصول'
    )
    count = models.IntegerField(default=1, verbose_name='تعداد')
    price = models.BigIntegerField(verbose_name='قیمت در زمان خرید')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')

    class Meta:
        verbose_name = 'محصول در سفارش'
        verbose_name_plural = '2. محصولات در سفارش'

    def total_price(self):
        return self.price * self.count

    def __str__(self):
        return f"{self.product} - {self.order}"
