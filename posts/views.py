from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

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
        serializer.data['owner'] = request.user.id
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PostDetailView(RetrieveAPIView):
    serializer_class = RetrievePostSerializer
    permission_classes = [IsAuthenticated]
