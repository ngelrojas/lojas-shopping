from rest_framework import generics
from core.models.user import User
from users.serializers import ActivateSerializer
from users.serializers import RActivateSerializer
from users.helper_views.helperActivate import HelperActivate


class SendEmailReAccount(generics.CreateAPIView):
    """
    send email to re-activate account
    """
    serializer_class = ActivateSerializer
    queryset = User.objects.all()


class ReactivateAccount(HelperActivate):
    """
    activate using token uid, to confirm
    email sent
    """
    serializer_class = RActivateSerializer
    queryset = User.objects.all()
