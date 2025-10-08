from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for comments.
    """
    author_username = serializers.ReadOnlyField(source='author.username')  # show username instead of id

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_username', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for posts, includes nested comments.
    """
    author_username = serializers.ReadOnlyField(source='author.username')  # show readable author
    comments = CommentSerializer(many=True, read_only=True)                # nested comments

    class Meta:
        model = Post
        fields = ['id', 'author', 'author_username', 'title', 'content', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['author', 'created_at', 'updated_at']
