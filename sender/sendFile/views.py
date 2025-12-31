from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Userdetails


@login_required(login_url='view_login')
def home(request):
    if request.method == "POST":
        file = request.FILES.get('file')
        if file:
            Userdetails.objects.create(user=request.user, file=file)
    
    
    show_file = Userdetails.objects.filter(user=request.user)

    context = {
        
        'show_file': show_file
    }

    return render(request, 'sendFile/home.html', context)


def view_login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        check_user = authenticate(request, username=username, password=password)

        if check_user:
            login(request, check_user)
            print("log in complate ")
            return redirect('home')
        else:
            print("password not match")
            return redirect('view_login')
        
    return render(request, 'sendFile/login.html')

def view_logout(request):
    logout(request)
    return redirect('view_login')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            return redirect('signup')

        if (password == password1):
            user = User.objects.create_user(username=username, password=password)
            Userdetails.objects.create(user=user, email=email)
            return redirect('view_login')

    return render(request, 'sendFile/signup.html')
