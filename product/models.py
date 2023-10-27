from django.db import models

# Create your models here.
from extensions.utils import upload_product_image_path


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    keywords = models.CharField(max_length=255, null=True, blank=True, verbose_name='کلمات کلیدی')
    price = models.BigIntegerField(verbose_name='قیمت', default=0)
    stock = models.IntegerField(verbose_name='موجودی در انبار', default=1)
    image = models.ImageField(upload_to=upload_product_image_path, verbose_name='تصویر محصول')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'جزئیات محصول'
        ordering = ('-created',)

    def __str__(self):
        return self.title
