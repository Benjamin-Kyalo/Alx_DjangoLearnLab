# Django CRUD Operations for Book Model

## 1. Create Operation

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected Output:
# <Book: 1984 by George Orwell (1949)>
```

````


## 2. Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
books
# Expected Output:
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>
```

---

## 3. Update Operation

```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()
book
# Expected Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
```

---

## 4. Delete Operation

```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
Book.objects.all()
# Expected Output:
# <QuerySet []>
````
