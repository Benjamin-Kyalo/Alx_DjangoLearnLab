# Social Media API - Task 0

## Overview

This project initializes a Django REST API for a social media platform.  
It includes user registration, login, token-based authentication, and profile management.

## Setup

1. Clone repo: `git clone https://github.com/<yourusername>/Alx_DjangoLearnLab`
2. Navigate to folder: `cd social_media_api`
3. Create & activate virtualenv, install dependencies
4. Run migrations:

python manage.py makemigrations
python manage.py migrate 5. Start server:

python manage.py runserver

## API Endpoints

| Endpoint                  | Method  | Description            |
| ------------------------- | ------- | ---------------------- |
| `/api/accounts/register/` | POST    | Register new user      |
| `/api/accounts/login/`    | POST    | Login and get token    |
| `/api/accounts/profile/`  | GET/PUT | View or update profile |

## Authentication

Use `Token <your_token>` in headers for authenticated endpoints.
