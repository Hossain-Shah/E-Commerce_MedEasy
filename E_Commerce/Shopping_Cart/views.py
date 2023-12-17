#importing libraries and frameworks
from django.shortcuts import render
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.generics import GenericAPIView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework.response import Response
from Shopping_Cart.serializers import ListSerializer
from Shopping_Cart.serializers import ProductSerializer
from Shopping_Cart.serializers import ListProductSerializer
from Shopping_Cart.models import Product
from rest_framework.decorators import api_view, permission_classes

#Product view for authorized customer
class ProductView(GenericAPIView):
    serializer_class = ListSerializer

    @permission_classes([IsAuthenticated])
    def get(self, request):
        request_data = request.query_params
        serializer = self.serializer_class(data=request_data)
        if not serializer.is_valid():
            print(serializer.errors)
            error_parameter = serializer.errors.popitem()[0]
            error_message = serializer.errors.popitem()[1][0]
            error_message = error_message
            data = {
                        "message": error_message,
                        "status": "error",
                        "status_code": status.HTTP_404_NOT_FOUND,
                   }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        
        name = serializer.validated_data.get("name")

        if name:
            products = Product.objects.filter(Q(name__icontains=name))
        else:
            products = Product.objects.all()

        serializer = ProductSerializer(products, many=True, context={"request": request})
        data = {
                    "message": "Successfully Retrieved",
                    "status": "success",
                    "status_code": status.HTTP_200_OK,
                    "data": serializer.data,
               }
        return Response(data, status=status.HTTP_200_OK)


#Product list for authorized customer
class ProductList(generics.ListAPIView):

    @permission_classes([IsAuthenticated])
    def get(self, request, format=None):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer(
            instance=queryset, many=True, context={"request": request}
        )
        products = Product.objects.all()
        serializer = ListProductSerializer(products, many=True, context={"request": request})
        data = {
                    "message": "Successfully Retrieved",
                    "status": "success",
                    "status_code": status.HTTP_200_OK,
                    "data": serializer.data,
               }
        return Response(data, status=status.HTTP_200_OK)

#Product detail
class ProductDetail(DetailView):
    model = Product
    template_name = 'product_details.html'


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

#Authorized customer login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
