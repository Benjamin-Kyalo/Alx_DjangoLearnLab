### **2. retrieve.md**

````markdown
# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve the specific book
book = Book.objects.get(title="1984")
book
# Expected Output:
# <Book: 1984 by George Orwell (1949)>
```
````
