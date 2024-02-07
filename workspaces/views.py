from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import WorkspaceOwnerSerializer, CreateUserSerializer
from workspaces.choices import RoleChoice
from workspaces.models import Workspace, WorkspaceRole, User
from django.db import transaction


class CreateWorkspaceView(CreateAPIView):
    serializer_class = WorkspaceOwnerSerializer
    queryset = Workspace.objects.all()

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            admin_ids = serializer.validated_data['admins']
            member_ids = serializer.validated_data['members']
            del serializer.validated_data['admins']
            del serializer.validated_data['members']
            workspace = serializer.save()
            WorkspaceRole(
                workspace=workspace,
                user=request.user,
                role=RoleChoice.OWNER
            ).save()
            for admin_id in admin_ids:
                try:
                    user = User.objects.get(id=admin_id)
                except User.DoesNotExist:
                    return Response(data=
                                    {"error": f"user {admin_id} does not exist"},
                                    status=status.HTTP_400_BAD_REQUEST)
                WorkspaceRole(
                    workspace=workspace,
                    user=user,
                    role=RoleChoice.ADMIN
                ).save()
            for member_id in member_ids:
                try:
                    user = User.objects.get(id=member_id)
                except User.DoesNotExist:
                    return Response(data=
                                    {"error": f"user {member_id} does not exist"},
                                    status=status.HTTP_400_BAD_REQUEST)
                WorkspaceRole(
                    workspace=workspace,
                    user=user,
                    role=RoleChoice.MEMBER
                ).save()
            return Response(status=status.HTTP_201_CREATED)


class SignUpView(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = []
