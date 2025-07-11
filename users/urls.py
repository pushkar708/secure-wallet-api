from django.urls import path
from .views import RegisterUser, LoginUser, AuthUser
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('.auth/me/', AuthUser.as_view(), name='auth_me'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
