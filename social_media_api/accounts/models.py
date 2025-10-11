from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model extending AbstractUser.
    Adds bio, profile picture, followers, and following fields.
    """
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following_users',
        blank=True
    )

    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followed_by',
        blank=True
    )

    def __str__(self):
        return self.username
