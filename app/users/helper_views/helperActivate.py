from rest_framework import viewsets
from core.encoder.tokens import decode_user_id
from rest_framework.response import Response
from core.models.user import User
from rest_framework import status
from users.helper_models.helperUser import HelperUser


class HelperActivate(viewsets.ModelViewSet):
    """update activate account """

    def update(self, request, **kwargs):
        """activate account using UID and token
        from email send user"""
        try:
            current = HelperUser()
            uid = decode_user_id(request.data.get('uid'))
            token = request.data.get('token')
            current_user = current.get_user_ID(uid)
            if not current_user.is_activate and token:
                current.re_activate_account(current_user.id)
                return Response({'data': 'user is activate.'},
                                status=status.HTTP_200_OK)
            return Response({'data': ' token expired. '})
        except User.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)
