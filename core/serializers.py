from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from core.models import User


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    password_repeat = serializers.CharField(write_only=True)

    def validate(self, attrs: dict) -> dict:
        if attrs.get('password') != attrs.get('password_repeat'):
            raise serializers.ValidationError('Пароли не совпадают!')
        return super().validate(attrs)

    def create(self, validated_data: dict) -> User:
        del validated_data['password_repeat']
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password_repeat',
        )
