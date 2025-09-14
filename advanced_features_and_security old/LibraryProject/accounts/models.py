from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
# Create a custom user manager
# This tells Django how to create normal users and superusers
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and return a regular user with email, username, and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)  # make email lowercase
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and return a superuser with all privileges.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)


# STEP 1: Define the custom user model
# We inherit from AbstractUser because we want to keep Django's default fields
# (username, password, first_name, last_name, email, etc.) and just add new ones.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)  # optional
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    # connect our custom manager
    objects = CustomUserManager()

    def __str__(self):
        return self.username
