from rest_framework import serializers

from core.models import User
from posts.models import Post


class ListPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name')

class RetrievePostSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
