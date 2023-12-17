#importing libraries and frameworks
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from Shopping_Cart.models import Product
from django.contrib.auth.models import User

#Serializing data-model
class ListSerializer(serializers.Serializer):
     name = serializers.CharField(max_length=100, required=False)


     def validate(self, attrs):
        name = attrs.get("name")
        return attrs

class ProductSerializer(serializers.ModelSerializer):
   customer_name = serializers.CharField(source="customer.name")
   customer_review = serializers.CharField(source="customer.review")

   class Meta:
        model = Product
        fields = [
                    "name",
                    "customer_name",
                    "availability",
                    "customer_review"
                 ]


class ListProductSerializer(serializers.ModelSerializer):
   customer_name = serializers.CharField(source="customer.name")
   customer_review = serializers.CharField(source="customer.review")

   class Meta:
        model = Product
        fields = [
                    "name",
                    "customer_name",
                    "customer_review"
                 ]

#Serializing authorized customers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
