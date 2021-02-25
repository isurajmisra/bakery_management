from rest_framework import serializers
from bakery_management.bakery.models import User


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'mobile', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mobile', 'email')