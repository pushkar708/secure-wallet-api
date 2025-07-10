from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUser, name='register'),
    path('login/', views.LoginUser, name='login'),
    path(".auth/me/", views.AuthUser.as_view(), name='auth_me'),
]
