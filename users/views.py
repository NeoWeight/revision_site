from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account Created! You can now log in')
            return redirect('login')
    else: 
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    user = get_object_or_404(User, username=request.user.username)
    context = {'user': user, 'posts': user.post_set.all()}
    return render(request, 'users/profile.html', context)

def profile_inspect(request, username):
    if request.user.is_authenticated:
        if request.user.username == username:
            return redirect('profile') 
    user = get_object_or_404(User, username=username)
    context = {'user': user, 'posts': user.post_set.all()}
    return render(request, 'users/profile_inspect.html', context)
