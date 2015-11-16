from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Item, Tag, Cart


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag', )


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    tags_set = TagSerializer(many=True)

    class Meta:
        model = Item
        fields = ('name', 'description', 'tags_set')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
