from django.shortcuts import render

# Create your views here.
class RegisterUser:
    def __init__(self, request):
        self.request = request

    def post(self):
        # Logic for registering a user
        pass

class LoginUser:
    def __init__(self, request):
        self.request = request

    def post(self):
        # Logic for logging in a user
        pass
    
class AuthUser:
    def __init__(self, request):
        self.request = request

    def get(self):
        # Logic for authenticating a user
        pass