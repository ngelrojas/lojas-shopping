from django.db import models
from autoslug import AutoSlugField
from core.models.user import User


class Product(models.Model):
    """model product"""
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title', always_update=True)
    excerpt = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    descount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    coupon = models.CharField(max_length=10, blank=True, default=0)
    stock = models.IntegerField(default=0)
    stock_min = models.IntegerField(default=0)
    stock_max = models.IntegerField(default=0)
    enable = models.BooleanField(default=True)
    users = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.users.first_name
