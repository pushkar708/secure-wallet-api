from django.contrib import admin
from django.urls import path, include

# Admin site branding (moved from settings.py)
admin.site.site_header = "Secure Wallet Admin"
admin.site.site_title = "Secure Wallet Admin Portal"
admin.site.index_title = "Welcome to Secure Wallet Admin"

urlpatterns = [
    path('api/v1/admin/', admin.site.urls)
]
