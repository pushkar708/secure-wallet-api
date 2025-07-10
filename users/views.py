from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

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
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        serializer = UserSerializer(user)
        refresh = RefreshToken.for_user(user)

        return Response({
            "user": serializer.data,
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }, status=status.HTTP_200_OK)