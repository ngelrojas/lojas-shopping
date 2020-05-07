from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

profileID = 2
CREATE_PROFILE_SELLER = reverse('profile:profile-seller')
UPDATE_PROFILE_SELLER = reverse('profile:profile-seller-detail',
                                args=[profileID])

PROFILE_BUYER = reverse('profile:profile-buyer', args=[profileID])


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class ProfileSellerTest(TestCase):

    def setUp(self):
        data = {
            'email': 'ngel@brasilprev.com',
            'password': 'me1234',
            'first_name': 'ngel',
            'last_name': 'brasilprev'}
        self.user = create_user(**data)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_profile_seller(self):
        """test create profile seller"""
        payload = {
            'dni': 'me@yopmail.com',
            'address': 'me1234',
            'country': 'me',
            'city': 'brasilprev',
            'zipcode': '123213',
            'cell_phone': '123654',
            'cnpj': '123654',
            'company_name': 'alkdj',
            'address_company': 'alksdj',
            'phone_company': '321654',
            'email_company': 'me@me.com'}
        res = self.client.post(CREATE_PROFILE_SELLER, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_get_profile_seller(self):
        """test get profile seller"""
        res = self.client.get(UPDATE_PROFILE_SELLER)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_profile_seller(self):
        """test create profile seller"""
        payload = {
            'dni': 'me@yopmail.com',
            'address': 'me1234',
            'country': 'me',
            'city': 'NEW DATa',
            'zipcode': '123213',
            'cell_phone': '123654',
            'cnpj': '987654',
            'company_name': 'alkdj',
            'address_company': 'alksdj',
            'phone_company': '321654',
            'email_company': 'me@me.com'}
        res = self.client.put(UPDATE_PROFILE_SELLER, payload)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_profile_buyer(self):
        """test get profile buyer"""
        res = self.client.get(PROFILE_BUYER)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_profile_buyer(self):
        """test update profile buyer"""
        payload = {
            'dni': 'me@yopmail.com',
            'address': 'me1234',
            'country': 'me',
            'city': 'NEW DATa',
            'zipcode': '123213',
            'cell_phone': '123654'}
        res = self.client.put(PROFILE_BUYER, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
