from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.models.product import Product
from core.models.queries.queryProduct import HelperProduct
from .serializers import ProductSerializer
from .helper_serializer.helperProduct import HelperSerializer


class ProductView(viewsets.ModelViewSet):
    """product view"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request):
        """list all products related user
        rules:
            - user not status deleted
            - user activated
        """
        try:
            queryset = HelperProduct.getAllProducts(self, request)
            serializer = self.serializer_class(queryset, many=True)
            return Response({'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk):
        try:
            current_user = HelperProduct.is_DeleteUser(self, request)
            current_product = HelperProduct.getProduct(self, current_user, pk)
            serializer = self.serializer_class(current_product)
            return Response({'data': serializer.data},
                            status=status.HTTP_200_OK)

        except Product.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """create product.
        rules:
            - user not status deleted
            - user activated
        """
        try:
            current_user = HelperProduct.is_DeleteUser(self, self.request)
            if current_user:
                HelperSerializer.save(self, request)
                return Response({'data': 'product created.'},
                                status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk):
        """update product for the current user
        rules:
            - user not status deleted
            - user activated
        """
        try:
            current_user = HelperProduct.is_DeleteUser(self, request)
            if current_user:
                HelperSerializer.update(self, request, pk)
                return Response({'data': 'product updated.'},
                                status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        """the method not deleted just disabled
        rules:
            - user not status deleted
            - user activated
        """
        try:
            current_user = HelperProduct.is_DeleteUser(self, request)
            if current_user:
                HelperSerializer.delete(self, request, pk)
                return Response({'data': 'product desabled.'},
                                status=status.HTTP_204_NO_CONTENT)
        except Exception as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)
