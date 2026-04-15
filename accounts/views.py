from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from accounts.forms import CustomUserChangeForm, ProfileForm


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
        return redirect('profile')
    return render(request, 'accounts/signup.html')


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')


@login_required
def edit_profile(request):
    user_form = CustomUserChangeForm(request.POST or None, instance=request.user)
    profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)

    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    return render(request, 'accounts/edit_profile.html', {
        'form': user_form,
        'profile_form': profile_form
    })


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('profile')
