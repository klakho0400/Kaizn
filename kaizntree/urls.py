from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ItemListAPIView, UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView, ItemListCreateAPIView, ItemRetrieveUpdateDestroyAPIView, UserLoginAPIView

urlpatterns = [
    path('api/items/', ItemListAPIView.as_view(), name='item-list'),
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('items/', ItemListCreateAPIView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemRetrieveUpdateDestroyAPIView.as_view(), name='item-detail'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
