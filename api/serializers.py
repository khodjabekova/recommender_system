from rest_framework import serializers

from products.models import Product, Review
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ('id', 'image', 'text', 'title', 'reviews')


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ('id','username')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    created_by = AuthorSerializer(source='author',many=False, read_only=True)
    product = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'product', 'created_by', 'rate', 'text')
