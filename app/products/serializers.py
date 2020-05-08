from rest_framework import serializers
from core.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    """serialzier model product"""
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'excerpt',
            'description',
            'price',
            'descount',
            'coupon',
            'enable',
            'stock',
            'stock_min',
            'stock_max')
