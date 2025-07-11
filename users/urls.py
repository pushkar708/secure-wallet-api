from django.urls import path
from .views import RegisterUser, LoginUser, AuthUser

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('.auth/me/', AuthUser.as_view(), name='auth_me')
]
