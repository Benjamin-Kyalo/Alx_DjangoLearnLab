from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    """
    Represents a user's post.
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,       # link to the custom user in accounts
        on_delete=models.CASCADE,       # delete post if author deleted
        related_name='posts'
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author.username}"


class Comment(models.Model):
    """
    Represents a comment on a post.
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,       # again, custom user from accounts
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
