from core.models.product import Product
from core.models.queries.queryUser import HelperUser


class HelperProduct(HelperUser):
    """helper queries"""
    def getAllProducts(self, request):
        user = HelperUser.is_DeleteUser(self, request)
        product = Product.objects.filter(users=user, enable=True)
        return product

    def getProduct(self, current_user, pk):
        product = Product.objects.get(
            id=pk, users=current_user, enable=True)
        return product
