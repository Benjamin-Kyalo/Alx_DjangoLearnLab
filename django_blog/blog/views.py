# blog/views.py
from django.shortcuts import render

def home(request):
    # This will render the base template
    return render(request, 'blog/base.html')
