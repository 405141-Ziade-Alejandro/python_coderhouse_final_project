from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Usuario o Contraseña incorrectos'
            })

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'accounts/login.html', {
                'error': 'Contraseñas no coinciden'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/login.html', {
                'error': 'Usuario ya existe'
            })

        user = User.objects.create_user(username, email, password1)

        login(request, user)
        return redirect('signup')
    return render(request, 'accounts/signup.html')


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')
