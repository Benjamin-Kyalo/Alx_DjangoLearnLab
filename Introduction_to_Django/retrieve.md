from bookshelf.models import Book

# Retrieve all books

books = Book.objects.all()
books

# Expected Output:

# <QuerySet [<Book: 1984 by George Orwell (1949)>]>
