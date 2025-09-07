from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # ---------------------------
    # Existing URLs
    # ---------------------------
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    # ---------------------------
    # Role-Based URLs (Task 3)
    # ---------------------------
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),

    # ---------------------------
    # Book Permission-Based URLs (Task 4)
    # ---------------------------
    path("book/add/", views.add_book, name="add_book"),
    path("book/<int:book_id>/edit/", views.edit_book, name="edit_book"),
    path("book/<int:book_id>/delete/", views.delete_book, name="delete_book"),
]
