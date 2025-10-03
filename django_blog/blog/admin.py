# blog/admin.py
from django.contrib import admin
from .models import Post

# Register the Post model so it appears in the Django admin
admin.site.register(Post)
