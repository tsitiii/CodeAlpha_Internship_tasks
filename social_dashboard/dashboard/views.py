from django.shortcuts import render, redirect
from .forms import *
from datetime import datetime
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    msg=None
    if request.method=='POST':
      form=SignUpForm(request.POST) 
      # now we can pass this obj to our template coz we inherited everything we need from the django default forms
      if form.is_valid():
        form.save()
        msg='user created'
        return redirect('login')
      else:
          msg='Form is invalid' 
    else:
        form=SignUpForm()
    context={'Form': form, 'msg': msg}
    return render(request, 'dashboard/register.html', context=context)




def Login(request):
    form = LoginForm()
    msg = None
    banned_msg = None  # Initialize banned message variable
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            Username = form.cleaned_data.get('username')
            Password = form.cleaned_data.get('password')
      
            user = authenticate(username=Username, password=Password)

            if user is not None:
                    return redirect('home')
            else:
                msg="error"
        else:
            msg = "Error while validating form!"
    
    context = {'form': form, 'msg': msg, 'banned_msg': banned_msg}  
    return render(request, 'dashboard/login.html', context=context)

def Home(request):
    return render(request, 'dashboard/home.html')

