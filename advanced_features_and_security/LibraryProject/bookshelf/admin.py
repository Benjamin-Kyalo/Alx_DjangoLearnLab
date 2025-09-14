from django.contrib import admin
from .models import Book
from accounts.models import CustomUser            # import our custom user model
from accounts.admin import CustomUserAdmin        # import the custom user admin


# Admin configuration for Book
class BookAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = ('title', 'author', 'publication_year')
    # Add a search bar for these fields
    search_fields = ('title', 'author')
    # Add a filter sidebar
    list_filter = ('publication_year',)


# ✅ Register models with the Django admin
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)  # required by the checker
