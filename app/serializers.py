from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import (User, Customer, Seller, Shop,
                     Category, Product, ProductImage,
                     Cart, CartItem, Order, OrderItem, Favourite)


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = []
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = super().create(**validated_data)
        if user.is_superuser == True:
            user.is_staff = True
        if password is not None:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        instance = super().update(instance, validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class CustomerSavingSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'phone', 'password',
                  'first_name', 'last_name', 'address')

    def create(self, validated_data):
        # Get the phone and password from the validated data
        phone = validated_data.pop('phone')
        password = validated_data.pop('password')

        # Check if a user already exists with the given phone
        if User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError(
                "A user with that phone already exists")

        # Create the user
        user = User(phone=phone, password=password)
        user.save()

        # Create the customer
        customer = Customer.objects.create(user=user, **validated_data)

        return customer

    def update(self, instance, validated_data):
        # Get the phone and password from the validated data
        phone = validated_data.pop('phone', None)
        password = validated_data.pop('password', None)

        if phone is not None:
            instance.user.phone = phone
            instance.user.save()

        if password is not None:
            instance.user.set_password(password)
            instance.user.save()

        for key in validated_data:
            setattr(instance, key, validated_data[key])

        return instance


class CustomerGetSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, source='user.phone')

    class Meta:
        model = Customer
        fields = ('username', 'first_name', 'last_name', 'address')


class SellerSavingSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = Seller
        fields = ('id', 'phone', 'password',
                  'first_name', 'last_name', 'certificate', 'address')

    def create(self, validated_data):
        # Get the phone and password from the validated data
        phone = validated_data.pop('phone')
        password = validated_data.pop('password')

        # Check if a user already exists with the given phone
        if User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError(
                "A user with that phone already exists")

        # Create the user
        user = User(phone=phone, password=password)
        user.save()

        # Create the customer
        seller = Seller.objects.create(user=user, **validated_data)

        return seller

    def update(self, instance, validated_data):
        # Get the phone and password from the validated data
        phone = validated_data.pop('phone', None)
        password = validated_data.pop('password', None)

        if phone is not None:
            instance.user.phone = phone
            instance.user.save()

        if password is not None:
            instance.user.set_password(password)
            instance.user.save()

        for key in validated_data:
            setattr(instance, key, validated_data[key])

        return instance


class SellerGetSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, source='user.phone')

    class Meta:
        model = Seller
        fields = ('username', 'first_name', 'last_name', 'address')


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        exclude = []


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = []


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = []


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = []


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        exclude = []


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        exclude = []


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        exclude = []


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = []


class FavouriteSerializer(ModelSerializer):
    class Meta:
        model = Favourite
        exclude = []
