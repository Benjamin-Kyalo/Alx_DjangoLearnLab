from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # Columns shown in the list view
    list_display = ('title', 'author', 'publication_year')  
    # Search bar for title & author
    search_fields = ('title', 'author')                     
    # Filter sidebar by year
    list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)
