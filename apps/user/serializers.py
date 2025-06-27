from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role,
                'badge_type': user.badge_type,
            }
        }


class SendReferralSerializer(serializers.Serializer):
    emails = serializers.ListField(
        child=serializers.EmailField(), allow_empty=False
    )
    badge_type = serializers.ChoiceField(
        choices=[('green', 'Green'), ('yellow', 'Yellow')],
        required=False
    )
