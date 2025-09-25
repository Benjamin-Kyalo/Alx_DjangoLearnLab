"""
API Views for Book Model

- BookListView: GET all books (open to all)
- BookDetailView: GET single book (open to all)
- BookCreateView: POST new book (authenticated only)
- BookUpdateView: PUT update book (authenticated only)
- BookDeleteView: DELETE a book (authenticated only)

Uses DRF generic views to handle CRUD operations efficiently.
"""


from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# =========================================
# LIST VIEW: Show all books (GET request)
# =========================================
class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Returns a list of all books.
    Accessible by anyone (no authentication required).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Open to all users

# =========================================
# DETAIL VIEW: Show a single book (GET request)
# =========================================
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<id>/
    Returns details of a single book.
    Accessible by anyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# =========================================
# CREATE VIEW: Add a new book (POST request)
# =========================================
class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Creates a new book.
    Only accessible by authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# =========================================
# UPDATE VIEW: Modify an existing book (PUT request)
# =========================================
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /api/books/<id>/update/
    Updates an existing book.
    Only accessible by authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# =========================================
# DELETE VIEW: Remove a book (DELETE request)
# =========================================
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<id>/delete/
    Deletes a book.
    Only accessible by authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
