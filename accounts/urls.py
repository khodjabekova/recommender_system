from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from accounts import views

app_name = 'accounts'

urlpatterns = [
    #path('login', views.login, name='login'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]