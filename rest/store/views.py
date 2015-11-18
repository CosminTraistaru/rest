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


class TagsViewSet(generics.ListCreateAPIView):
    """
    List all items from a specific tag.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

    def filter_queryset(self, queryset):
        return queryset.filter(tags__tag=self.kwargs['pk'])


class SingleItemViewSet(generics.ListCreateAPIView):
    """
    List all items from a specific tag.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

    def filter_queryset(self, queryset):
        return queryset.filter(name=self.kwargs['pk'])


class SearchItemsViewSet(generics.ListCreateAPIView):
    """
    List all items from a specific tag.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

    def filter_queryset(self, queryset):
        return queryset.filter(name__contains=self.kwargs['pk'])