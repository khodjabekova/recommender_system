from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('users/register/', views.UserCreate.as_view()),
    path('login/', obtain_auth_token),
    path('products/', views.ProductList.as_view()),
    path('products/<pk>/', views.ProductDetail.as_view()),
    path('reviews/<pk>/', views.ProductReviews().as_view()), #Get and Post

]