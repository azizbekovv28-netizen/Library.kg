from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from users.models import CustomUser
from users.forms import CustomRegisterForm, CustomAuthLoginForm


def register_view(requset):
    if requset.method == "POST":
        form_user = CustomRegisterForm(requset.POST, requset.FILES)
        if form_user.is_valid():
            form_user.save()
            return redirect ('/login/')
    else:
        form_user = CustomRegisterForm
    return render (requset, 'users/register.html', {'form': form_user})

def auth_login_view(request):
    if request.method == "POST":
        form_user = CustomAuthLoginForm(data=request.POST)
        if form_user.is_valid():
            user = form_user.get_user()
            login(request, user)
            return redirect('/profile/')
    else:
        
        form_user = CustomAuthLoginForm()
    return render(request, 'users/login.html', {'form': form_user})


def auth_logout_view(request):
    logout(request)
    return redirect('/login/')

#
def profile_view(request):
    if not request.user.is_authenticated:
        return ('/login/')
    user = CustomUser.objects.get(id=request.user.id)
    return render(request, 'users/profile.html', {'user': user})

