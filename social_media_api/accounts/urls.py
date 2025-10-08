from django.urls import path                                # import path for routing
from .views import RegisterView, LoginView, ProfileView      # import our views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # register endpoint
    path('login/', LoginView.as_view(), name='login'),           # login endpoint
    path('profile/', ProfileView.as_view(), name='profile'),     # profile view/update endpoint
]
