#importing libraries
from django.urls import path
 
from Shopping_Cart.views import ProductDetail
from Shopping_Cart.views import ProductView
from Shopping_Cart.views import ProductList
from . import views
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI

#paths
urlpatterns = [
    path('product', ProductList.as_view()),
    path('api/product', ProductView.as_view()),
    path('product/<int:pk>', ProductDetail.as_view()),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall')
]