# api/views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# -------------------------------
# LIST VIEW
# -------------------------------
class BookListView(generics.ListAPIView):
    """
    View to list ALL books in the system.
    Anyone can access this endpoint.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# -------------------------------
# DETAIL VIEW
# -------------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve ONE book by its ID (primary key).
    Example: /books/1/ will return the book with ID=1.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# -------------------------------
# CREATE VIEW
# -------------------------------
class BookCreateView(generics.CreateAPIView):
    """
    View to CREATE a new book entry.
    Requires sending book data (title, publication_year, author).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# -------------------------------
# UPDATE VIEW
# -------------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    View to UPDATE an existing book.
    Example: /books/update/1/ will update the book with ID=1.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# -------------------------------
# DELETE VIEW
# -------------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    View to DELETE a book by ID.
    Example: /books/delete/1/ will delete the book with ID=1.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
