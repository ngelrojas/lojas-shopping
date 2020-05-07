from rest_framework import serializers
from core.models.profile import ProfileBuyer
from users.serializers import UserSerializer


class ProfileBuyerSerializer(serializers.ModelSerializer):
    """serializer profile user buyer"""
    users = UserSerializer(read_only=True)

    class Meta:
        model = ProfileBuyer
        fields = (
            'dni',
            'address',
            'country',
            'city',
            'zipcode',
            'cell_phone',
            'users')
