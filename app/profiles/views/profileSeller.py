from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.models.profile import ProfileSeller
from profiles.serializers.profileSeller import ProfileSellerSerializer
from core.models.queries.queryProfile import HelperProfile
from core.models.queries.queryProfile import HelperProfileSeller


class ProfileSellerView(viewsets.ModelViewSet):
    """profile seller view"""
    serializer_class = ProfileSellerSerializer
    queryset = ProfileSeller.objects.all()
    userseller = True
    userbuyer = False

    def retrieve(self, request, pk=None):
        """get current profile user seller
        rules:
            - user not status deleted
            - user activated
        """
        try:
            current_profile = HelperProfileSeller.getProfileSeller(
                self, request, self.userseller)
            serializer = self.serializer_class(current_profile)
            return Response({'data': serializer.data},
                            status=status.HTTP_200_OK)
        except ProfileSeller.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer):
        """create profile seller
        rules:
            - user not delete status
            - user activated
        """
        try:
            current_profile = HelperProfile.getProfile(
                self, self.request, self.userbuyer)
            if current_profile:
                return serializer.save(users=self.request.user)
        except ProfileSeller.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """update profile seller user
        rules:
            - user not status deleted
            - user activated
            - typeuser True
        """
        try:
            current_profile = HelperProfileSeller.getProfileSeller(
                self, request, self.userseller)
            serializer = self.serializer_class(
                current_profile,
                data=request.data,
                partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'data': 'profile seller updated.'},
                                status=status.HTTP_200_OK)
        except ProfileSeller.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)
