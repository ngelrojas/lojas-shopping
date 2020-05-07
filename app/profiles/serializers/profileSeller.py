from rest_framework import serializers
from core.models.profile import ProfileSeller


class ProfileSellerSerializer(serializers.ModelSerializer):
    """serializer profile user seller"""

    class Meta:
        model = ProfileSeller
        fields = (
            'dni',
            'address',
            'country',
            'city',
            'zipcode',
            'cell_phone',
            'cnpj',
            'company_name',
            'address_company',
            'phone_company',
            'email_company')
