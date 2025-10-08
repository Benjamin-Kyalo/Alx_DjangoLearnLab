from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD endpoints for posts.
    """
    queryset = Post.objects.all().order_by('-created_at')      # newest first
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # anyone can read, only auth users can write
    filter_backends = [filters.SearchFilter]                      # enables ?search=
    search_fields = ['title', 'content']                          # searchable fields

    def perform_create(self, serializer):
        """
        Called when creating a new post — attach current user as author.
        """
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """
        Ensure only post author can edit.
        """
        if self.request.user != serializer.instance.author:
            raise PermissionError("You can only edit your own posts.")
        serializer.save()


class CommentViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD endpoints for comments.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Attach the logged-in user as the comment author.
        """
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """
        Ensure only comment author can edit.
        """
        if self.request.user != serializer.instance.author:
            raise PermissionError("You can only edit your own comments.")
        serializer.save()
