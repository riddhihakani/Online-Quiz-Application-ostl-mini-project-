from django.contrib.auth.models import User
from profiles.models import Profile
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponseRedirect, request
from django.contrib.auth import login, logout
from django.urls import reverse_lazy

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = User.objects.last()
            profile = Profile(user=user)
            profile.save()
            #log user in
            login(request,user)
            return redirect('student:dash')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
           #log in user
            user = form.get_user()
            login(request,user)
            if request.user.is_staff:
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('tutor:dash')
            else:
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('student:dash')

    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):

        logout(request)
        return redirect('homepage')
