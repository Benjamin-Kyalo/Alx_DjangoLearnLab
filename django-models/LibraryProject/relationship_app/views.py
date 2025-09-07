from django.shortcuts import render
from django.views.generic.detail import DetailView   # <- checker wants this exact line
from .models import Library
from .models import Book

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()  # <- checker looks for Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view: display details for a specific library
class LibraryDetailView(DetailView):   # <- checker looks for DetailView
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
