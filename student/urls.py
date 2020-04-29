from django.urls import path,re_path
from . import views


app_name = 'student'

urlpatterns = [
    path('',views.student_dash,name="dash"),
    path('course_list/',views.course_list,name="courselist"),
    path('heading_list/<int:id>/',views.heading_list,name="headinglist"),
    path('question_list/<int:id>/',views.question_list,name="questions"),
    path('result/',views.result,name="result"),
    
]