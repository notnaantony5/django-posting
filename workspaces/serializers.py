from rest_framework import serializers
from workspaces.models import Workspace, User


class WorkspaceOwnerSerializer(
    serializers.ModelSerializer):
    admins = serializers.ListField(
        child=serializers.IntegerField()
    )
    members = serializers.ListField(
        child=serializers.IntegerField()
    )

    class Meta:
        model = Workspace
        fields = '__all__'


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
