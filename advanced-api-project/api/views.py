# api/views.py
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ✅ List all books OR create a new one
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can add, everyone can view
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# ✅ Update a book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can update
    permission_classes = [permissions.IsAuthenticated]

# ✅ Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only staff (e.g., admins) can delete
    permission_classes = [permissions.IsAdminUser]
