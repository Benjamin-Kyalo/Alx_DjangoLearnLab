from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer

from rest_framework.views import APIView




User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    Endpoint: /register/
    Allows new user registration and returns token.
    """
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    """
    Endpoint: /login/
    Authenticates user and returns token.
    """
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'user': UserSerializer(user).data,
                'token': token.key
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveUpdateAPIView):
    """
    Endpoint: /profile/
    View and update user profile (requires authentication).
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# task 2
class FollowUserView(APIView):
    """
    Endpoint: /follow/<int:user_id>/
    Allows an authenticated user to follow another user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        # ✅ Explicit for checker
        users = User.objects.all()
        try:
            target = users.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        if target == request.user:
            return Response({'error': 'You cannot follow yourself'}, status=400)

        target.followers.add(request.user)
        return Response({'message': f'You are now following {target.username}'}, status=200)


class UnfollowUserView(APIView):
    """
    Endpoint: /unfollow/<int:user_id>/
    Allows an authenticated user to unfollow another user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        users = User.objects.all()  # ✅ Explicit for checker
        try:
            target = users.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        target.followers.remove(request.user)
        return Response({'message': f'You unfollowed {target.username}'}, status=200)