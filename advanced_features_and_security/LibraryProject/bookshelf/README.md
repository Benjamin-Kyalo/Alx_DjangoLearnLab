# LibraryProject

This is my first Django project for the ALX Django Learn Lab.

- Installed Django and verified setup
- Created project `LibraryProject` with default structure
- Verified the development server is running

## Security Best Practices

- DEBUG = False for production
- Enabled protections: XSS filter, content type nosniff, clickjacking denial
- CSRF tokens added in all forms
- Cookies secured: CSRF_COOKIE_SECURE, SESSION_COOKIE_SECURE
- ORM used instead of raw SQL (prevents injection)
- Optional: CSP via django-csp middleware
