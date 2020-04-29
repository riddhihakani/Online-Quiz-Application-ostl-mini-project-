from django import forms
from .models import Profile




class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['fname','lname','email','profession','degree','state','nationality','city','profile_img','bio','college']
        labels = {
            'fname' : 'FIRST NAME',
            'lname' : 'LAST NAME',
            'email' : 'EMAIL',
            'college' : 'INSTITUTE',
            'profession' : 'PROFESSION',
            'degree' : 'DEGREE',
            'state'  : 'STATE',
            'nationality' : 'NATIONALITY',
            'city' : 'CITY',
            'profile_img' : 'PROFILE IMAGE',
            'bio':'BIO',

           
        }

