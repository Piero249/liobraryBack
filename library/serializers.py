
from django.contrib.auth.models import User, Group
from .models import Book
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    """ Serializer for User """

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):

    """ Serializer for Group """

    class Meta:
        model = Group
        fields = ['url', 'name']


class BookSerializer(serializers.ModelSerializer):

    """Serializer for Book"""

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_year', 'edition',
        'image', 'stock']