from django.contrib.auth.models import User
from .serializers import UserSerializer, ItemSerializer
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Item


class UserViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def retrieve(self, request, *args, **kwargs):
        queryset = User.objects.all().order_by('-date_joined')
        user = get_object_or_404(queryset, pk=args[0])
        serializer = UserSerializer(user)
        return Response(serializer.data)


class ItemViewSet(generics.GenericAPIView):
    """
    List all items.
    """
    serializer_class = ItemSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)

