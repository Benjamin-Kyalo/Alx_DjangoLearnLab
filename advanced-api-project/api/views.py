# api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated  # ✅ add this
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

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
    permission_classes = [IsAuthenticatedOrReadOnly]  # ✅ only authenticated users can modify data


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
    permission_classes = [IsAuthenticatedOrReadOnly]  # ✅ only authenticated users can modify data


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
    permission_classes = [IsAuthenticated]  # ✅ only authenticated users can create data


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
    permission_classes = [IsAuthenticated]  # ✅ only authenticated users can update data


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
    permission_classes = [IsAuthenticated]  # ✅ only authenticated users can delete data
