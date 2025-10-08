# import base user class
from django.contrib.auth.models import AbstractUser  
# import Django ORM tools
from django.db import models                         

class CustomUser(AbstractUser):
    """
    This class extends Django's built-in AbstractUser.
    We add extra fields to support social media features like bio, profile picture, and followers.
    """

    bio = models.TextField(blank=True, null=True)  
    profile_picture = models.ImageField(           
        upload_to='profile_pics/',                 # uploaded images go to /media/profile_pics/
        blank=True, 
        null=True
    )
    followers = models.ManyToManyField(            # other users who follow this user
        'self',                                    # reference same model
        symmetrical=False,                         # relationship is one-way (A follows B doesn't mean B follows A)
        related_name='following',                  # allows reverse lookup (user.following.all())
        blank=True
    )

    def __str__(self):
        """
        Returns the username when printing the user object.
        """
        return self.username
