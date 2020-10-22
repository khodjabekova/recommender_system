from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductList.as_view(), name='all'),
   
    path('create/', views.CreateProduct.as_view(), name='create'),
    path('edit/<pk>', views.UpdateProduct.as_view(), name='edit'),
    path('delete/<pk>', views.DeleteProduct.as_view(), name='delete'),
    path('<pk>/', views.ProductDetail.as_view(), name='detail'),
    path('review/<pk>/', views.add_review_to_product, name='add_review_to_product'),
    path('review/<pk>/delete/', views.review_remove, name='delete_review'),
]