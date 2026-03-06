from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Books
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    mybooks = {
        'all_book': Books.objects.all()
    }
    return render(request, 'index.html', mybooks)
def userlogin(request):
    # If user is authenticated user can't redirect to login page
    if request.user.is_authenticated:
        return redirect('/')
    # 
    if request.method == 'POST':
        username = request.POST.get('username') # this username is from login form
        password = request.POST.get('pass') # this password is from login form
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/') # redirect to home page
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')
def logoutuser(request):
    logout(request)
    return redirect('/login')