from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = []

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = super().create(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

    def update(self, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user
