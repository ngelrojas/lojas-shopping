from products.serializers import ProductSerializer
from core.models.product import Product


class HelperSerializer:
    """class helper to save product"""
    def save(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            product_save = Product.objects.create(
                title=request.data.get('title'),
                excerpt=request.data.get('excerpt'),
                description=request.data.get('description'),
                price=request.data.get('price'),
                descount=request.data.get('descount'),
                coupon=request.data.get('coupon'),
                stock=request.data.get('stock'),
                stock_min=request.data.get('stock_min'),
                stock_max=request.data.get('stock_max'),
                users=request.user)
        return product_save

    def update(self, request, pk):
        product_save = Product.objects.get(
            id=pk, users=request.user)
        serializer = ProductSerializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            product_save.title = request.data.get('title')
            product_save.excerpt = request.data.get('excerpt')
            product_save.description = request.data.get('description')
            product_save.price = request.data.get('price')
            product_save.descount = request.data.get('descount')
            product_save.coupon = request.data.get('coupon')
            product_save.stock = request.data.get('stock')
            product_save.stock_min = request.data.get('stock_min')
            product_save.stock_max = request.data.get('stock_max')
            product_save.save()
            return product_save

    def delete(self, request, pk):
        product_enable = Product.object.get(
            id=pk, users=request.user)
        product_enable.enable = False
        product_enable.save()
        return product_enable
