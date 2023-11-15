from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import managers # we will write this file shortly


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    gender = models.CharField(
        max_length=140,
        null=True,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        )
    )
    # picture = models.models.ImageField(upload_to='uploads/% Y/% m/% d/')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.CustomUserManager()

    def __str__(self):
        return f"{self.email}'s custom account"
    
class Author(models.Model):
    name = models.CharField(verbose_name='نویسنده',max_length=255,blank=True,null=True,default='author')

class Category(models.Model):
    name = models.CharField(verbose_name='دسته بندی',max_length=255,blank=True,null=True,default='category')

class Publisher(models.Model):
    name = models.CharField(verbose_name='منتشر کننده',max_length=255,blank=True,null=True,default='publisher')

class Book(models.Model):
    title = models.CharField(verbose_name='عنوان',max_length=255,blank=True,null=True,default='title')
    author = models.ForeignKey(to=Author,on_delete=models.CASCADE,verbose_name='نویسنده')
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE,verbose_name='دسته بندی')
    publisher = models.ForeignKey(to=Publisher,on_delete=models.CASCADE,verbose_name='منتشر کننده')
    publisherDate = models.DateTimeField(auto_now_add=True,verbose_name='زمان انتشار')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='قیمت')
    description = models.TextField(verbose_name='توضیحات')

class Customer(models.Model):
    user = models.ForeignKey(to=CustomUser,on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='ایمیل')
    address = models.CharField(verbose_name='ادرس',max_length=255,blank=True,null=True,default='address')
    phone = models.CharField(verbose_name='تماس',max_length=255,blank=True,null=True,default='phone')

class Order(models.Model):
    book = models.ManyToManyField(to=Book,through='OrderItem',verbose_name='کتاب')
    customer = models.ForeignKey(to=Customer,on_delete=models.CASCADE,verbose_name='فروشنده')
    totalPrice = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='قیمت')
    orderDate = models.DateTimeField(auto_now_add=True,verbose_name='زمان سفارش')

class OrderItem(models.Model):
    book = models.ForeignKey(to=Book,on_delete=models.CASCADE,verbose_name='کتاب')
    order = models.ForeignKey(to=Order,on_delete=models.CASCADE,verbose_name='سفارش')
    quantity = models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='قیمت')