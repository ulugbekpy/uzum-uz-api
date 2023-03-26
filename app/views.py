from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from .serializers import (UserSerializer, CustomerSavingSerializer,
                          CustomerGetSerializer,
                          SellerSavingSerializer, SellerGetSerializer, ShopSerializer,
                          ProductSerializer, ProductImageSerializer, CategorySerializer,
                          CartSerializer, OrderSerializer, FavouriteSerializer)
from .models import (User, Customer, Seller, Shop,
                     Category, Product, ProductImage,
                     Cart, Order, Favourite)
from .pagination import DefaultPagination
from .filters import ProductFilter


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
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['category', 'price', 'shop']


class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


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
