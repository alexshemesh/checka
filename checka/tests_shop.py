from django.test import TestCase
from . models import PaymentCheck, Shop
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from PIL import Image
import tempfile
from django.contrib.auth.models import User


class ShopModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="someuser")
        Shop.objects.create(name='Some Shop', type="whatever", owner=user)

    def test_we_can_get_data_at_all(self):
        checks = Shop.objects.order_by('date_added')
        self.assertEqual(checks.__len__(), 1)

    def test_we_can_get_some(self):
        checks = Shop.objects.filter(name='Some Shop')
        self.assertEqual(checks.__len__(), 1)
        self.assertEqual(checks[0].name, 'Some Shop')


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.client = APIClient()


        self.shop_data = {'name': 'some shop', 'type': 'goodone' }
        self.response = self.client.post(
            reverse('checka:create'),
            self.shop_data,
            format = 'multipart')

    def test_api_can_create_a_shop(self):
        """Test the api has check creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

