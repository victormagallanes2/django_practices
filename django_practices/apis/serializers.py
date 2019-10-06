from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Products


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ProductsListSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = (
                  'id',
                  'name',
                  'quantity',
                  'price',
                  'description',
                  'picture'
                  )

class ProductsDetailSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = (
                  'id',
                  'name',
                  'quantity',
                  'price',
                  'description',
                  'picture'
                  )


class ProductsCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = (
                  'name',
                  'quantity',
                  'price',
                  'description'
                  )