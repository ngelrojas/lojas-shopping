from rest_framework import serializers
from core.models.order import Order
from products.serializers import ProductSerializer
from core.models.product import Product


class OrderSerializer(serializers.ModelSerializer):
    """serializer order model"""
    products = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Product.objects.all())

    class Meta:
        model = Order
        fields = (
            'id',
            'title',
            'description',
            'enable',
            'products')


class OrderDetail(serializers.ModelSerializer):
    """detail order model"""
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'title',
            'description',
            'enable',
            'products')
