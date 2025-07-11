from django.contrib import admin
from django.urls import path, include

api_patterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('wallets/', include('wallets.urls')),
]

urlpatterns = [
    path('api/v1/', include(api_patterns)),
]
