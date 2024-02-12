# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from .models import Item, User
# from .serializers import ItemSerializer, UserSerializer, UserLoginSerializer
# from rest_framework_simplejwt.tokens import AccessToken

# class BaseAuthenticatedAPITest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create(username='test_user', password='test_password')
#         self.token = AccessToken.for_user(self.user)

#     def get_authenticated_client(self):
#         self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
#         return self.client

# class UserLoginAPIViewTest(BaseAuthenticatedAPITest):
#     def test_user_login_valid_credentials(self):
#         url = reverse('user-login')
#         data = {'username': 'test_user', 'password': 'test_password'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_user_login_invalid_credentials(self):
#         url = reverse('user-login')
#         data = {'username': 'test_user', 'password': 'wrong_password'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

# class UserListCreateAPIViewTest(BaseAuthenticatedAPITest):
#     def test_user_list(self):
#         url = reverse('user-list-create')
#         response = self.get_authenticated_client().get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     # Add more tests for create functionality if needed

# class UserRetrieveUpdateDestroyAPIViewTest(BaseAuthenticatedAPITest):
#     def test_user_retrieve(self):
#         url = reverse('user-detail', kwargs={'pk': self.user.pk})
#         response = self.get_authenticated_client().get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     # Add more tests for update and destroy functionality if needed

# class ItemListCreateAPIViewTest(BaseAuthenticatedAPITest):
#     def test_item_list(self):
#         url = reverse('item-list-create')
#         response = self.get_authenticated_client().get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     # Add more tests for create functionality if needed

# class ItemRetrieveUpdateDestroyAPIViewTest(BaseAuthenticatedAPITest):
#     def setUp(self):
#         super().setUp()
#         self.item = Item.objects.create(name='Test Item')

#     def test_item_retrieve(self):
#         url = reverse('item-detail', kwargs={'pk': self.item.pk})
#         response = self.get_authenticated_client().get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     # Add more tests for update and destroy functionality if needed

# class ItemListAPIViewTest(BaseAuthenticatedAPITest):
#     def setUp(self):
#         super().setUp()
#         self.item = Item.objects.create(name='Test Item')

#     def test_item_list_filtering(self):
#         url = reverse('item-list')
#         response = self.get_authenticated_client().get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     # Add more tests for pagination and filtering if needed
