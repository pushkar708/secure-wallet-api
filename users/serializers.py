from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from wallets.models import Wallet
from rest_framework.validators import UniqueValidator

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), message="Email already exists.")]
    )
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Wallet.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'date_joined']
