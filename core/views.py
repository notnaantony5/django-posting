from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers import SignUpSerializer
class SignUpView(CreateAPIView):
    serializer_class = SignUpSerializer
    def post(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
