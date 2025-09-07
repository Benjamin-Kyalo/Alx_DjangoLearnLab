from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, permission_required  # <-- important import

# ---------------------------
# Existing Views
# ---------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# ---------------------------
# Task 3: Role-Based Access Views
# ---------------------------
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

# ---------------------------
# Task 4: Book Permission-Based Views
# ---------------------------
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        library_id = request.POST.get("library")
        library = get_object_or_404(Library, id=library_id)
        Book.objects.create(title=title, author=author, library=library)
        return redirect("list_books")
    libraries = Library.objects.all()
    return render(request, "relationship_app/add_book.html", {"libraries": libraries})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        library_id = request.POST.get("library")
        book.library = get_object_or_404(Library, id=library_id)
        book.save()
        return redirect("list_books")
    libraries = Library.objects.all()
    return render(request, "relationship_app/edit_book.html", {"book": book, "libraries": libraries})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})
