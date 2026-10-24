from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import CustomizedUserSignUp
from . models import User
from . authenticate import Auth
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db import transaction

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        b = authenticate(request,username=email,password=password)

        if b is not None:
            login(request,b)
            res = redirect('profile')
            res.set_cookie('c_k','c1',max_age=120,httponly=True)
            return res
        else:
              return render(request, 'pages/login.html', {
                'error': 'Authentication failed. Check your custom backend logic.'
            })


    return render(request,'pages/login.html')

def register(request):
    if request.method == "POST":
        new_user = CustomizedUserSignUp(request.POST)
        if new_user.is_valid():
            new_user.save()
            new_user.email_automation()
            return redirect('mainpage')

    else:
        new_user = CustomizedUserSignUp()
    return render(request,"pages/register.html",{"form":new_user})

@require_POST
def logout_user(request):
    logout(request)

    res = redirect('mainpage')
    res.delete_cookie('c_k')
    return res

@login_required
def profile(request):
    return render(request,"pages/dashboard.html")
