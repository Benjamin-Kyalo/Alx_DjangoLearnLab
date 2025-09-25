# Advanced API Project

Part of **Alx_DjangoLearnLab** — demonstrates Django REST Framework APIs with CRUD, filtering, searching, ordering, and unit testing.

## Features

- Author & Book CRUD APIs
- Filtering (`?author=`), searching (`?search=`), ordering (`?ordering=`) on books
- Permissions: authenticated users required for create/update/delete
- Unit tests for Authors and Books

## Quick Setup

```bash
git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/advanced-api-project
python -m venv venv
# activate venv:
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API Endpoints

**Authors**

- `GET /api/authors/`
- `GET /api/authors/<id>/`
- `POST /api/authors/create/` (auth required)
- `PUT /api/authors/update/<id>/` (auth required)
- `DELETE /api/authors/delete/<id>/` (auth required)

**Books**

- `GET /api/books/` — supports `?search=`, `?author=`, `?ordering=`
- `GET /api/books/<id>/`
- `POST /api/books/create/` (auth required)
- `PUT /api/books/update/<id>/` (auth required)
- `DELETE /api/books/delete/<id>/` (auth required)

## Tests (file: `api/test_views.py`)

This project contains unit tests for both Authors and Books using DRF's `APITestCase`. Tests exercise:

- **Authors**

  - List authors
  - Retrieve author
  - Create (requires authentication)
  - Update (requires authentication)
  - Delete (requires authentication)

- **Books**

  - List books
  - Retrieve a book
  - Create (requires authentication)
  - Update (requires authentication)
  - Delete (requires authentication)
  - Filtering by `publication_year` and `author`
  - Searching by `title` (partial match via DRF `SearchFilter`)
  - Ordering by fields (e.g. `title`, `publication_year`)

Tests live in `api/test_views.py` and are written to run against Django's automatic **test database** (so your dev data remains safe).

## Run Tests

```bash
python manage.py test api
```

This command:

- Creates a temporary test database,
- Runs the tests in `api/test_views.py`,
- Prints results and then destroys the test database.
