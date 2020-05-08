from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.models.order import Order
from core.models.queries.queryOrder import HelperOrder
from .serializers import OrderSerializer
from .serializers import OrderDetail


class OrderView(viewsets.ModelViewSet):
    """
    viewset order
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def list(self, request):
        """list all orders by user
        rules:
            - user not status deleted
            - user activated
        """
        try:
            queryset = HelperOrder.getAllOrder(self, request)
            serializer = OrderDetail(queryset, many=True)
            return Response({'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Order.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        """get a order by user
        rules:
            - user not status deleted
            - user activated
        """
        try:
            current_user = HelperOrder.is_DeleteUser(self, request)
            current_order = HelperOrder.getOrder(self, current_user, pk)
            serializer = OrderDetail(current_order)
            return Response({'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Order.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer):
        """create order
        rules:
            - user not status deleted
            - user activated
        """
        try:
            current_user = HelperOrder.is_DeleteUser(self, self.request)
            if current_user:
                return serializer.save(users=current_user)
        except Exception as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk):
        """update order
        rules:
            - user not status deleted
            - user activated
        """
        try:
            current_user = HelperOrder.is_DeleteUser(self, request)
            current_order = HelperOrder.getOrder(self, current_user, pk)
            if current_user:
                serializer = self.serializer_class(
                    current_order,
                    data=request.data,
                    partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({'data': 'order update.'},
                                    status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        """disable order
        rules:
            - user not status deleted
            - user activated
        """
        try:
            current_user = HelperOrder.is_DeleteUser(self, request)
            if current_user:
                HelperOrder.deleteOrder(self, request, pk)
                return Response({'data': 'order update.'},
                                status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)
