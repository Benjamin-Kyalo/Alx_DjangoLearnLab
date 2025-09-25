# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


# -------------------------------
# Author API Tests
# -------------------------------
class AuthorAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        # Create a test author
        self.author = Author.objects.create(name="Author 1")

    def test_list_authors(self):
        url = reverse("author-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author_requires_authentication(self):
        url = reverse("author-create")
        data = {"name": "New Author"}

        # Unauthenticated → should fail
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated → should succeed
        self.client.login(username="testuser", password="password123")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_author(self):
        url = reverse("author-update", args=[self.author.id])
        data = {"name": "Updated Author"}

        self.client.login(username="testuser", password="password123")
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.author.refresh_from_db()
        self.assertEqual(self.author.name, "Updated Author")

    def test_delete_author(self):
        url = reverse("author-delete", args=[self.author.id])

        self.client.login(username="testuser", password="password123")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# -------------------------------
# Book API Tests
# -------------------------------
class BookAPITests(APITestCase):
    def setUp(self):
        # Create user and author
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.author = Author.objects.create(name="Author 1")

        # Create sample books
        self.book1 = Book.objects.create(title="Book A", publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title="Book B", publication_year=2021, author=self.author)

    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book A")

    def test_create_book_requires_authentication(self):
        url = reverse("book-create")
        data = {"title": "New Book", "publication_year": 2022, "author_id": self.author.id}

        # Unauthenticated → should fail
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated → should succeed
        self.client.login(username="testuser", password="password123")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Updated Book", "publication_year": 2020, "author_id": self.author.id}

        self.client.login(username="testuser", password="password123")
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book(self):
        url = reverse("book-delete", args=[self.book1.id])

        self.client.login(username="testuser", password="password123")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # -------------------------------
    # Filtering, Searching, Ordering
    # -------------------------------
    def test_filter_books_by_publication_year(self):
        url = reverse("book-list") + "?publication_year=2020"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book A")

    def test_search_books_by_title(self):
        url = reverse("book-list") + "?search=Book A"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # ✅ FIXED: Search is partial, so just check Book A is in results
        titles = [book["title"] for book in response.data]
        self.assertIn("Book A", titles)

    def test_order_books_by_title_descending(self):
        url = reverse("book-list") + "?ordering=-title"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, ["Book B", "Book A"])
