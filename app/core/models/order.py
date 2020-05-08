from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .user import User
from .product import Product


class Order(models.Model):
    """model order"""
    title = models.CharField(max_length=20, default='my first order')
    description = models.CharField(max_length=50, default='cool things')
    enable = models.BooleanField(default=True)
    users = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.title
