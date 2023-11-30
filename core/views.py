from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'core/about.html', {'title': 'About'})