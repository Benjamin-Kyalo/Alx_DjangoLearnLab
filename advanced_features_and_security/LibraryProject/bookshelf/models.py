from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# STEP 1: Create a custom user manager
# This controls how Django creates users and superusers.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and return a regular user.
        - username: required
        - email: required (normalized to lowercase)
        - password: securely hashed
        - extra_fields: any additional fields (like date_of_birth)
        """
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)  # normalize email (makes lowercase, etc.)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # password is hashed, not stored raw
        user.save(using=self._db)    # save to database
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


# STEP 2: Define the custom user model
# We extend AbstractUser to keep Django's default fields (username, password, etc.)
# and add our extra fields.
class CustomUser(AbstractUser):
    # new fields we need
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    # link our custom manager
    objects = CustomUserManager()

    def __str__(self):
        # string representation in admin and shell
        return self.username
