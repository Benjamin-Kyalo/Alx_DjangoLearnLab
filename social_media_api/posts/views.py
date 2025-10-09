from rest_framework import viewsets, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# ✅ New addition for Task 2
class FeedView(APIView):
    """
    Endpoint: /feed/
    Returns posts from users that the current user follows.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get all users the current user follows
        following_users = request.user.following.all()
        # Fetch posts authored by followed users
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        # Serialize post data
        serializer = PostSerializer(posts, many=True)
        # Return serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)
