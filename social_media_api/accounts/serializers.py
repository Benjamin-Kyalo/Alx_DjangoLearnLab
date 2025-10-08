from rest_framework import serializers                     # DRF serializers
from django.contrib.auth import get_user_model              # import dynamic user model
from rest_framework.authtoken.models import Token           # import token model

User = get_user_model()                                     # get custom user model


class RegisterSerializer(serializers.ModelSerializer):
    """
    Handles user registration and token creation.
    """

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture')

    def create(self, validated_data):
        """
        Create a new user instance and generate a token.
        """
        # ✅ We explicitly call get_user_model().objects.create_user() 
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        Token.objects.create(user=user)                     # generate token
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Returns user profile details.
    """
    followers_count = serializers.SerializerMethodField()   # computed field for follower count

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers_count')

    def get_followers_count(self, obj):
        return obj.followers.count()
