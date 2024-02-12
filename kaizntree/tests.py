from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import Item, User
from .serializers import ItemSerializer, UserSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from .views import (
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView,
    ItemListCreateAPIView,
    ItemRetrieveUpdateDestroyAPIView,
    ItemListAPIView,
    CustomPagination
)
class BaseTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

class UserLoginAPIViewTests(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create(username='testuser', password='testpassword')

    def test_user_login_valid_credentials(self):
        url = reverse('user-login')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_login_invalid_credentials(self):
        url = reverse('user-login')
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'Wrong Password')

    def test_user_login_user_doesnt_exist(self):
        url = reverse('user-login')
        data = {'username': 'nonexistentuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'User doesnt Exist')

class UserListCreateAPIViewTests(APITestCase):
    def setUp(self):
        self.user_data = {'username': 'testuser', 'password': 'testpassword', 'name' : 'testname', 'email': 'abc123@test.com'}

    def test_create_user_authenticated(self):
        url = reverse('user-list-create')
        response = self.client.post(url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PermissionsTest(TestCase):

    def test_user_retrieve_update_destroy_api_permissions(self):
        view = UserRetrieveUpdateDestroyAPIView()
        permissions = view.permission_classes
        self.assertIn(IsAuthenticated, permissions)

    def test_item_list_create_api_permissions(self):
        view = ItemListCreateAPIView()
        permissions = view.permission_classes
        self.assertIn(IsAuthenticated, permissions)

    def test_item_retrieve_update_destroy_api_permissions(self):
        view = ItemRetrieveUpdateDestroyAPIView()
        permissions = view.permission_classes
        self.assertIn(IsAuthenticated, permissions)

    def test_item_list_api_permissions(self):
        view = ItemListAPIView()
        permissions = view.permission_classes
        self.assertIn(IsAuthenticated, permissions)
