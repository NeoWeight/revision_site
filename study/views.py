from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'study/home.html', {'title': 'Home'})

def resources(request):
    return render(request, 'study/resources.html', {'title': 'Resources'})