from django.contrib.auth.models import User
from .serializers import UserSerializer, ItemSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Item


class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class ItemViewSet(generics.ListCreateAPIView):
    """
    List all items.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)
