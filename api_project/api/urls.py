from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
# create a router
router = DefaultRouter()
# link router to BookViewSet
router.register(r'books_all', BookViewSet, basename='book_all')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'), # for ListAPIView
    path('', include(router.urls)), # include the router URLs
]
