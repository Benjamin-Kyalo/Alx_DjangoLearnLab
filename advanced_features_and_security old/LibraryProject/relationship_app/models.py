from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# ---------------------------
# Library & Book Models
# ---------------------------
class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

# ---------------------------
# UserProfile for Role-Based Access
# ---------------------------
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    ]
    # Use settings.AUTH_USER_MODEL so it works with a swapped user model
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Member")

    def __str__(self):
        # guard in case user deleted (shouldn't happen because on_delete is CASCADE)
        return f"{getattr(self.user, 'username', str(self.user))} - {self.role}"

# Automatically create profile for each new user
User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, role="Member")
