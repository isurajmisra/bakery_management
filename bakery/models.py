from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(max_length=15, blank=False, null=True)
    role = models.CharField(max_length=20, blank=False, null=True)


    def __str__(self):
        return self.username


    class Meta:
        db_table = 'user'


class Ingredient(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ingredient'


class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    ingredient = models.ManyToManyField(Ingredient)
    quantity = models.IntegerField()
    discount = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    class Meta:
        db_table = 'product_price'
