from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import (User, Customer, Seller, Shop,
                     Category, Product, ProductImage,
                     Cart, CartItem, Order, OrderItem, Favourite)
from .serializers import (UserSerializer, CustomerSavingSerializer, CustomerGetSerializer,
                          SellerSavingSerializer, SellerGetSerializer, ShopSerializer,
                          ProductSerializer, ProductImageSerializer, CategorySerializer,
                          CartSerializer, OrderSerializer, CartItemSerializer,
                          OrderItemSerializer, FavouriteSerializer)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import ProductFilter
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
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']


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


class CategoryViewSet(ViewSet):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySerializer
    pagination_class = None

    def get_queryset(self):
        return self.queryset.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
