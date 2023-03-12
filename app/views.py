from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_context(self):
        return {'request': self.request}
