from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from core.models.user import User
from core.models.queries.queryUser import HelperUser
from .serializers import UserSerializer
from .serializers import RecoveryPwdSerializer
from .serializers import PwdConfirmSerialzier
from .helper_views.helperRecoveryPwd import HelperRecoveryPWD
from .helper_views.helperUpdateUser import HelperUpdateUser


class CreateUserView(generics.CreateAPIView):
    """Create new user"""
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UpdateUserView(viewsets.ModelViewSet):
    """update main data current user"""
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def retrieve(self, request, pk=None):
        """
        retrieve current user using rules:
        - user not status deleted
        """
        try:
            current_user = HelperUser.is_DeleteUser(self, request)
            serializer = self.serializer_class(current_user)
            return Response({'data': serializer.data},
                            status=status.HTTP_200_OK)
        except User.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """update data partial current user"""
        try:
            current_user = HelperUpdateUser.UpdateUser(
                self, request, self.serializer_class)
            if current_user:
                return Response({'data': 'data updated.'},
                                status=status.HTTP_200_OK)
            return Response({'error': 'data not update.'},
                            status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        """update state current user to deleted"""
        try:
            HelperUser.delete_user(self, request)
            return Response({'data': 'user deleted'},
                            status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)


class RecoveryPasswordUser(viewsets.ModelViewSet):
    """recovery send email current user password"""
    serializer_class = RecoveryPwdSerializer
    queryset = User.objects.all()


class RecoveryPwdConfirm(viewsets.ModelViewSet):
    """recovery password confirmations"""
    serializer_class = PwdConfirmSerialzier
    queryset = ''

    def update(self, request, **kwargs):
        """method to recovery - change password user"""
        try:
            current_user = HelperRecoveryPWD.helperUpdate(
                self, request, self.serializer_class)
            if current_user:
                return Response({'data': 'password changed.'},
                                status=status.HTTP_200_OK)
            return Response({'error': 'password not changed'},
                            status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)
