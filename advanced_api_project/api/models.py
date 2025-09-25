from django.db import models
from django.core.exceptions import ValidationError
import datetime

# Author model stores information about book authors
class Author(models.Model):
    name = models.CharField(max_length=255)  # Name of the author

    def __str__(self):
        return self.name  # Display author name in admin

# Book model stores information about books
class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title
    publication_year = models.IntegerField()  # Year book was published
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    # related_name allows Author to access all their books with author.books.all()

    def __str__(self):
        return self.title

    # Custom validation to ensure publication year is not in the future
    def clean(self):
        current_year = datetime.datetime.now().year
        if self.publication_year > current_year:
            raise ValidationError("Publication year cannot be in the future.")
