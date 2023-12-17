from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from app.models import Product, CartItem, Cart, Wishlist
from app.models import User


class RegisterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', "username", 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        hashed_password = make_password(password)
        user = User.objects.create(**validated_data,
                                   password=hashed_password)
        return user


class LoginModelSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise serializers.ValidationError("Incorrect credentials")
        else:
            raise serializers.ValidationError("Both username and password are required")

        data['user'] = user
        return data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['user', 'items']


class WishlistSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    items = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = ['user', 'items']
