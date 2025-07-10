from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RegisterUser(APIView):
    def get(self, request):
        return Response({"message": "User registration page"}, status=status.HTTP_200_OK)

    def post(self, request):
        # Logic for registering a user
        return Response({"message": "User registered"}, status=status.HTTP_201_CREATED)


class LoginUser(APIView):
    def post(self, request):
        # Logic for logging in a user
        return Response({"message": "User logged in"}, status=status.HTTP_200_OK)


class AuthUser(APIView):
    def get(self, request):
        # Logic for checking authentication
        return Response({"authenticated": True}, status=status.HTTP_200_OK)
