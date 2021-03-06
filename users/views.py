from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, Group
from django.shortcuts import render, redirect
from django.urls import reverse

from . import forms


def login_user_view(request):
    """
    Loging authenticated user and redirecting to home page if logged successfully else reject login

    Using Form object to validate data

    Using cleaned_data to normalize data
    """
    if request.method == 'POST':
        form = forms.LoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(email=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('home:home'))
    else:
        form = forms.LoginForm()

    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    """
    Logging out authenticated user
    """
    logout(request)
    return redirect(reverse('users:login'))


def registration_view(request):
    """
    Register user using RegistrationForm, checking for permissions and adding user to preferred group

    Using Form to validate data

    Using cleaned_data to normalize data
    """
    form = forms.RegistrationForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            if form.cleaned_data['is_owner'] is True:
                permission = Permission.objects.get(name='Can add camping')
                owner_group = Group.objects.get(name='owners')
                user.groups.add(owner_group)
                user.user_permissions.add(permission)
            else:
                permission = Permission.objects.get(name='Can view camping')
                regular_group = Group.objects.get(name='regular')
                user.groups.add(regular_group)
                user.user_permissions.add(permission)
            return redirect(reverse('users:login'))
    return render(request, 'users/registration.html', {'form': form})
