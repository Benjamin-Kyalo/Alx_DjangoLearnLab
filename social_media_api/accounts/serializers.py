# import DRF serializers
from rest_framework import serializers
# get the custom user model dynamically                  
from django.contrib.auth import get_user_model 
# model used for token-based auth         
from rest_framework.authtoken.models import Token       

# fetch the custom user model
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for handling user registration.
    Converts JSON input into a new user object and returns user data after creation.
    """
    password = serializers.CharField(write_only=True)   # ensure password isn't exposed in responses

    class Meta:
        model = User                                    # use our custom user model
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture')

    def create(self, validated_data):
        """
        This method creates a new user instance when registration happens.
        """
        user = User.objects.create_user(                # create user with hashed password
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        Token.objects.create(user=user)                 # create authentication token
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying user profile info.
    """
    followers_count = serializers.SerializerMethodField()  # computed field

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers_count')

    def get_followers_count(self, obj):
        """
        Returns number of followers for the user.
        """
        return obj.followers.count()
