from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'forum/home.html', context)


def about(request):
    return render(request, 'forum/about.html', {'title': 'About'})

def base(request):
    return render(request, 'forum/base.html', {'title': 'About'})