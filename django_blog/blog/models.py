# blog/models.py
from django.db import models
from django.contrib.auth.models import User  # built-in User model for authors

class Post(models.Model):
    # Title of the blog post
    title = models.CharField(max_length=200)
    
    # Content/body of the post
    content = models.TextField()
    
    # Auto-set the date when the post is first published
    published_date = models.DateTimeField(auto_now_add=True)
    
    # Link each post to a user (author). If user is deleted, delete their posts too.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        # This makes the post title show up nicely in the admin panel
        return self.title
