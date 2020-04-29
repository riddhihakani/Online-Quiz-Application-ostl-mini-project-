from django.shortcuts import render
from tutor.models import Course
from tutor.models import Heading
from tutor.models import Quest

# Create your views here.

def student_dash(request):
    return render(request,'student/student_dashboard.html')


def course_list(request):
    context = {'course_list':Course.objects.all() }
    return render(request,'student/course_list.html', context)


def heading_list(request,id):
    context = {'heading_list' : Heading.objects.all().filter(course = id)}
    return render(request,'student/heading_list.html',context)


def question_list(request,id):
    context = {'question_list' : Quest.objects.all().filter(heading = id)}
    return render(request,'student/question_list.html',context)
  


def result(request):
    return render(request,'student/result.html')


