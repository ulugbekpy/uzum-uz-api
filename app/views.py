from rest_framework.viewsets import ModelViewSet
from .models import (User, Customer, Seller, Shop,
                     Category, Product, ProductImage,
                     Cart, CartItem, Order, OrderItem, Favourite)
from .serializers import (UserSerializer, CustomerSavingSerializer, CustomerGetSerializer,
                          SellerSavingSerializer, SellerGetSerializer, ShopSerializer,
                          ProductSerializer, ProductImageSerializer,
                          CartSerializer, OrderSerializer, CartItemSerializer,
                          OrderItemSerializer, FavouriteSerializer)
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


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class FavouriteViewSet(ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
