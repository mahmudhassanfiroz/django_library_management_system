from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from . forms import SignUpForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password='password1')
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request,'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')
