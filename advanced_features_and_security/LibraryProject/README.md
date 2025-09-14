# Advanced Features and Security — Permissions & Groups

## Overview

This project demonstrates **managing permissions and groups in Django**.  
Users are assigned to groups (Editors, Viewers, Admins), and permissions control access to views.

---

## Custom Permissions

Defined in `bookshelf/models.py`:

- `can_view` → Can view books
- `can_create` → Can create books
- `can_edit` → Can edit books
- `can_delete` → Can delete books

---

## Groups

Configured via **Django Admin**:

- **Viewers** → has `can_view`
- **Editors** → has `can_create`, `can_edit`
- **Admins** → has all permissions

---

## Views

In `bookshelf/views.py`, permissions are enforced with decorators:

- `@permission_required('bookshelf.can_view')` → protects `book_list`
- `@permission_required('bookshelf.can_create')` → protects `add_book`
- `@permission_required('bookshelf.can_edit')` → protects `edit_book`

---

## Testing

1. Create test users in Dja
