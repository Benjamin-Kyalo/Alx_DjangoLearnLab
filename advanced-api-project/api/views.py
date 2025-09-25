# api/views.py

from rest_framework import generics, filters  # ✅ added filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as django_filters  # ✅ required for filtering
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# -------------------------------
# AUTHOR VIEWS
# -------------------------------
class AuthorListView(generics.ListAPIView):
    """
    View to list ALL authors.
    Anyone can access this endpoint.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorDetailView(generics.RetrieveAPIView):
    """
    View to retrieve ONE author by ID.
    Example: /authors/1/
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorCreateView(generics.CreateAPIView):
    """
    View to CREATE a new author.
    Example: POST {"name": "New Author"}
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class AuthorUpdateView(generics.UpdateAPIView):
    """
    View to UPDATE an existing author.
    Example: /authors/update/1/
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class AuthorDeleteView(generics.DestroyAPIView):
    """
    View to DELETE an author.
    Example: /authors/delete/1/
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


# -------------------------------
# BOOK VIEWS
# -------------------------------
class BookListView(generics.ListAPIView):
    """
    View to list ALL books in the system.
    Supports filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # ✅ filtering, searching, ordering (Task 2)
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["title", "author", "publication_year"]
    search_fields = ["title", "author__name"]
    ordering_fields = ["title", "publication_year"]


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
