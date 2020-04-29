from django.urls import path
from . import views
from django.conf.urls import include


app_name = 'profiles'

urlpatterns = [
    path('profileform/',views.profileform,name="profileform"),
    path('myprofile/',views.myprofile,name="myprofile"),
    # path('editprofile/<int:id>/',views.editprofile,name="editprofile"),
    
]