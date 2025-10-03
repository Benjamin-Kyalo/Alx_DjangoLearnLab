from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver

from taggit.managers import TaggableManager

class Post(models.Model):
    # Title of the blog post
    title = models.CharField(max_length=200)
    
    # Content/body of the post
    content = models.TextField()
    
    # Auto-set the date when the post is first published
    published_date = models.DateTimeField(auto_now_add=True)
    
    # Link each post to a user (author). If user is deleted, delete their posts too.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tags = TaggableManager()

    def __str__(self):
        # This makes the post title show up nicely in the admin panel
        return self.title
    def get_absolute_url(self):
        
        # Redirects to the detail page of this post after save
        return reverse("post-detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

    def get_absolute_url(self):
        # Redirect back to the post detail page after saving a comment
        return reverse("post-detail", kwargs={"pk": self.post.pk})
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

# Automatically create or update profile when user is created/updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()