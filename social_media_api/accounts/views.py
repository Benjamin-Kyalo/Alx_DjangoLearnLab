from rest_framework import generics, permissions, status             # DRF view helpers
from rest_framework.response import Response                         # for API responses
from rest_framework.authtoken.models import Token                    # token model
from django.contrib.auth import authenticate                         # handles login
from .serializers import RegisterSerializer, UserSerializer           # import our serializers
from django.contrib.auth import get_user_model                        # get user model dynamically

User = get_user_model()  # get our custom user model


class RegisterView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    POST request with username, email, password creates a new user + token.
    """
    serializer_class = RegisterSerializer                             # specify serializer
    permission_classes = [permissions.AllowAny]                       # anyone can register

    def create(self, request, *args, **kwargs):
        """
        Custom response: return user data and token after successful registration.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)                     # validate input
        user = serializer.save()                                      # save user to DB
        token, created = Token.objects.get_or_create(user=user)       # get or create auth token
        return Response({
            "user": UserSerializer(user).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    """
    API endpoint for user login.
    POST request with username and password returns authentication token.
    """
    serializer_class = RegisterSerializer                             # reuse fields for validation
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")                       # get username
        password = request.data.get("password")                       # get password
        user = authenticate(username=username, password=password)     # verify credentials

        if user:
            token, _ = Token.objects.get_or_create(user=user)         # return existing/new token
            return Response({
                "token": token.key,
                "user": UserSerializer(user).data
            })
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveUpdateAPIView):
    """
    API endpoint for viewing and updating user profile.
    Only accessible to authenticated users.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]                # must be logged in

    def get_object(self):
        """
        Returns the logged-in user object.
        """
        return self.request.user
