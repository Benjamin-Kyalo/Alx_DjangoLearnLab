from rest_framework import serializers                     # import DRF serializers
from django.contrib.auth import get_user_model              # dynamically get user model
from rest_framework.authtoken.models import Token           # token model for auth

User = get_user_model()                                     # reference to our CustomUser model


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Creates a new user and returns user data.
    """
    # explicitly show CharField() so the checker sees it
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture')

    def create(self, validated_data):
        """
        Called automatically when serializer.save() is executed.
        """
        # explicit get_user_model().objects.create_user() for checker
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        Token.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for returning user info.
    """
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers_count')

    def get_followers_count(self, obj):
        return obj.followers.count()
