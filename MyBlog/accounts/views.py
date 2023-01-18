from django.shortcuts import render

# Create your views here.


def login_view(request):
    return render('login.html',)

def logout_view(request):
    pass

def signup_view(request):
    return render('signup.html')
