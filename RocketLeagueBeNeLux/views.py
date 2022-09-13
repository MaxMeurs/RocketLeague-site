from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .decorater import *
from django.core.mail import send_mail


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'klant'])
def home(request):
    return render(request, 'BeNeLux/home.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'klant'])
def settings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'BeNeLux/settings.html', context)

@unauthenticated_user
def registeerpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'account was gemaakt voor ' + username)

            return redirect('login')
        else:
            messages.info(request, 'account is niet gelukt, probeer het nog eens')

    context = {'form': form}
    return render(request, 'BeNeLux/registreer.html', context)

@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username of password in incorect')

    context = {}
    return render(request, 'BeNeLux/login.html', context)


@login_required(login_url='login')
def logoutusers(request):
    logout(request)
    return redirect('login')