from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(max_length=10)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

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
    ingredient = models.ManyToManyField(Ingredient, related_name='product_ingredients')
    ingredient_details = models.JSONField(blank=False, null=True)
    discount = models.IntegerField(default=0,blank=False, null=True)
    cost_price = models.FloatField(default=0, blank=False, null=True)
    selling_price = models.FloatField(default=0, blank=False, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, related_name='products_order')
    products_details = models.JSONField(blank=False, null=True)
    total_price = models.FloatField(default=0, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + '-' + str(self.total_price)

    class Meta:
        db_table = 'order'


