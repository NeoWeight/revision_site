from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Neo',
        'title': 'Welcome to Revision Goat!',
        'content': 'First post content',
        'date_posted': 'November 29, 2023'
    },
    {
        'author': 'Jane Doe',
        'title': 'Help me revise!!!',
        'content': 'Second post content',
        'date_posted': 'November 29, 2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'forum/home.html', context)


def about(request):
    return render(request, 'forum/about.html', {'title': 'About'})