from django.shortcuts import render,redirect
from .forms import ProfileForm
from .models import Profile




def profileform(request):
    if request.method == 'GET':
        form = ProfileForm()
        return render(request,'profiles/profileform.html',{'form' : form})
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('profiles:myprofile')


def myprofile(request):
    
    return render(request,'profiles/myprofile.html')



