from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.models.profile import ProfileBuyer
from core.models.queries.queryProfile import HelperProfile
from profiles.serializers.profileBuyer import ProfileBuyerSerializer


class ProfileBuyerView(viewsets.ModelViewSet):
    """profile buyer view"""
    serializer_class = ProfileBuyerSerializer
    queryset = ProfileBuyer.objects.all()
    userbuyer = False

    def retrieve(self, request, pk=None):
        """
        get profile current user
        @typeuser=False
        """
        try:
            current_profile = HelperProfile.getProfile(
                self, request, self.userbuyer)
            serializer = self.serializer_class(current_profile)
            return Response({'data': serializer.data},
                            status=status.HTTP_200_OK)
        except ProfileBuyer.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """
        update profile current user
        rules:
            - user not status deleted
            - user activated
            - typeuser False
        """
        try:
            current_profile = HelperProfile.getProfile(
                self, request, self.userbuyer)
            serializer = self.serializer_class(
                current_profile,
                data=request.data,
                partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'data': 'profile buyer update.'},
                                status=status.HTTP_200_OK)
        except ProfileBuyer.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)
