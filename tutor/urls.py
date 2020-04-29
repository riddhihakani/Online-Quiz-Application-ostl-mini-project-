from django.urls import path
from . import views



app_name = 'tutor'

urlpatterns = [
    path('',views.tutor_dash,name="dash"),
    path('addnewcourse/',views.addcourse,name="newcourse"),
    path('addnewheading/',views.addheading,name="newheading"),
    path('addnewquestion/',views.addquest,name="newquest"),
    path('courselist/',views.courselist,name="courselist"),
    path('course_delete/<int:id>/',views.course_del,name="coursedelete"),
    path('course_details/<int:id>/',views.course_detail,name="coursedetails"),
    path('heading_delete/<int:id>/',views.heading_del,name="headingdelete"),
    path('heading_details/<int:id>/',views.heading_detail,name="headingdetails"),
    path('update_question/<int:id>/',views.update_question,name="updatequestion"),
    path('question_delete/<int:id>/',views.question_del,name="deletequestion"),
   
   
]
