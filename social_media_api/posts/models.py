from django.db import models                           # import Django ORM
from django.conf import settings                        # lets us access AUTH_USER_MODEL dynamically
from django.utils import timezone                       # for timestamps


class Post(models.Model):
    """
    Represents a social-media post.
    """
    author = models.ForeignKey(                         # who wrote it
        settings.AUTH_USER_MODEL,                       # link to our custom user
        on_delete=models.CASCADE,                       # delete posts if user deleted
        related_name='posts'                            # allows user.posts.all()
    )
    title = models.CharField(max_length=255)             # short post title
    content = models.TextField()                         # main post body
    created_at = models.DateTimeField(default=timezone.now)  # creation timestamp
    updated_at = models.DateTimeField(auto_now=True)     # auto-update when edited

    def __str__(self):
        return f"{self.title} by {self.author.username}"


class Comment(models.Model):
    """
    Represents comments on posts.
    """
    post = models.ForeignKey(                            # which post it belongs to
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(                          # who commented
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    content = models.TextField()                         # comment body
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
