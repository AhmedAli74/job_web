from django.http import Http404
from django.shortcuts import render,redirect
from .forms import Signup,User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signup(request):
    if request.method=='POST':
        sign=Signup(request.POST)
        if sign.is_valid:
            sign.save()
            return redirect('Home:home')
    else:
        sign=Signup()
    context={
        'sign':sign
    }
    return render(request,'accounts/signup.html',context)
def logiin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username and password:
            log=authenticate(username=username,password=password)
            if log is not None:
                login(request,log)
                return redirect('Home:home')
            else:
                return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
        else:
            raise Http404('page not found')
    return render(request,'accounts/login.html')

def logoutt(request):
    logout(request)
    return redirect('accounts:login')

def reset_password(request):
    if request.method=='POST':
        email=request.POST['email']
        password1=request.POST['password']
        confirm_pass=request.POST['password2']
        if password1 == confirm_pass:
            user_exist=User.objects.filter(email=email).exists()
            if user_exist:
                user=User.objects.get(email=email)
                user.set_password(password1)
                user.save()
                return redirect('accounts:login')
    return render(request,'accounts/reset_password.html')