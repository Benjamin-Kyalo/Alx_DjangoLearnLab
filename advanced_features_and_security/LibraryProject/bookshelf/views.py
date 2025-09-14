from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book


# STEP 3.1: Only users with "can_view" can see the book list
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # safe query
    return render(request, "bookshelf/book_list.html", {"books": books})


# STEP 3.2: Only users with "can_create" can add a book
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # just a placeholder view for now
    return render(request, "bookshelf/form_example.html")


# STEP 3.3: Only users with "can_edit" can edit a book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # just a placeholder view
    return render(request, "bookshelf/form_example.html")



# Safe view — no raw SQL
def book_list(request):
    # ✅ Using Django ORM prevents SQL injection
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


def search_books(request):
    query = request.GET.get("q", "")
    # ✅ ORM with filter, not raw query
    books = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/book_list.html", {"books": books})
