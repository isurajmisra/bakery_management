from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'mobile', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data['password'] == validated_data['confirm_password']:
            validated_data.pop('confirm_password', None)
            user = super().create(validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user
        else:
            raise Exception


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'mobile', 'email')