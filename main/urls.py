# your_app_name/urls.py

from django.urls import path
from .views import UserRegisterView, CustomTokenObtainPairView, LogoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
