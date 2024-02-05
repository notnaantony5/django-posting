from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from core.models import User
from posts.models import Post
from posts.serializers import (
    ListPostSerializer,
    PostSerializer,
    RetrievePostSerializer
)


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = ListPostSerializer
    permission_classes = []


class PostCreateView(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.validated_data['owner'] = request.user
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = RetrievePostSerializer
    permission_classes = [IsAuthenticated]


class Posts(APIView):
    def get(self, request, *args, **kwargs):
        user1 = User(
            username="sasha",
            password="<PASSWORD>"
        )
        user2 = User(
            username="petya",
            password="<PASSWORD>"
        )
        post = Post(
            title="test",
            content="test",
        )
        user1.save()
        user2.save()
        post.save()
        post.owners.set([user1, user2])
        post.save()
