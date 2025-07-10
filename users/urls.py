from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('.auth/me/', views.AuthUser.as_view(), name='auth_me'),
]
