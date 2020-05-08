from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from core.models.product import Product

productID = 1
PRODUCT_URL = reverse('product:product')
PRODUCT_URL_DETAIL = reverse('product:product-detail', args=[productID])


def create_user(**params):
    return get_user_model().objects.create_user(**params)


def create_product(user):
    return Product.objects.create(
        title="fist product",
        excerpt="fist product excerpt",
        description="first product description",
        price=54.25,
        descount=5,
        coupon="125adsd",
        stock=20,
        stock_min=5,
        stock_max=50,
        users=user)


class ProductTest(TestCase):

    def setUp(self):
        data = {
            'email': 'ngel@brasilprev.com',
            'password': 'me1234',
            'first_name': 'ngel',
            'last_name': 'brasilprev'}
        self.user = create_user(**data)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_product_user(self):
        """test create product"""
        payload = {
            'title': 'fist product',
            'excerpt': 'excerpt product',
            'description': ' description ',
            'price': 45,
            'descount': 45,
            'coupon': '123654',
            'stock': 45,
            'stock_min': 45,
            'stock_max': 45,
            'users': self.user}
        res = self.client.post(PRODUCT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_list_product_user(self):
        """test get list product per user"""
        res = self.client.get(PRODUCT_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_product_user(self):
        """test get retrieve product"""
        res = self.client.get(PRODUCT_URL_DETAIL)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_product_user(self):
        """test create product"""
        payload = {
            'title': 'NEW product',
            'excerpt': 'excerpt product',
            'description': ' description ',
            'price': 45,
            'descount': 45,
            'coupon': '123654',
            'stock': 45,
            'stock_min': 45,
            'stock_max': 45,
            'users': self.user}
        res = self.client.put(PRODUCT_URL_DETAIL, payload)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
