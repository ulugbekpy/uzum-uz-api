from rest_framework.viewsets import ModelViewSet
from .models import User, Customer, Seller
from .serializers import UserSerializer, CustomerSavingSerializer, CustomerGetSerializer, SellerSavingSerializer, SellerGetSerializer
# from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return CustomerSavingSerializer
        return CustomerGetSerializer


class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return SellerSavingSerializer
        return SellerGetSerializer
