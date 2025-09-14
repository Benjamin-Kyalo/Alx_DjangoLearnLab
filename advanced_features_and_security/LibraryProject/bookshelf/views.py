from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm   # ✅ import ExampleForm


# STEP 3.1: Only users with "can_view" can see the book list
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # safe ORM query
    return render(request, "bookshelf/book_list.html", {"books": books})


# STEP 3.2: Only users with "can_create" can add a book
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():  # ✅ safe form validation
            # For demo: just return form data to template
            return render(request, "bookshelf/form_example.html", {
                "form": form,
                "message": "Form submitted successfully!"
            })
    else:
        form = ExampleForm()
    return render(request, "bookshelf/form_example.html", {"form": form})


# STEP 3.3: Only users with "can_edit" can edit a book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    form = ExampleForm()  # placeholder form
    return render(request, "bookshelf/form_example.html", {"form": form})


# ✅ Safe search view (uses ORM, not raw SQL)
def search_books(request):
    query = request.GET.get("q", "")
    books = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/book_list.html", {"books": books})
