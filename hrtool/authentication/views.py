from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm


def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials.'})
    else:
        return render(request, 'login.html')


def my_logout(request):
    logout(request)
    return redirect('index')


def my_create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'create.html', {'form': form})
