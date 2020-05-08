from core.models.order import Order
from core.models.queries.queryUser import HelperUser


class HelperOrder(HelperUser):
    """helper queries"""
    def getAllOrder(self, request):
        """get all orders related current user"""
        user = HelperUser.is_DeleteUser(self, request)
        order_user = Order.objects.filter(users=user, enable=True)
        return order_user

    def getOrder(self, current_user, pk):
        """get order related a user and order ID"""
        order_user = Order.objects.get(
            id=pk,
            users=current_user,
            enable=True)
        return order_user

    def deleteOrder(self, current_user, pk):
        """disable order current user"""
        order_user = self.getOrder(current_user, pk)
        order_user.enable = False
        order_user.save()
        return order_user
