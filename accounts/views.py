from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import UserRegisterForm

# Create your views here.
""" def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(Q(email=username) | Q(username=username)).first()
            if user_obj and password:
                user = authenticate(request,username=user_obj.username,password=password)
                if  user is not None:
                    login(request,user)
                    messages.success(request, 'Welcome back! You have successfully logged in.')
                    return redirect('/')
        return render(request,'accounts/login.html')
    else:
        return redirect('/')
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'You have successfully signed up!')
                return redirect('/')
        else:
            form = UserRegisterForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')
"""

