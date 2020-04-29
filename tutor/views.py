from django.shortcuts import render,redirect
from .forms import CourseForm
from .forms import HeadingForm
from .forms import QuestionForm
from .models import Course
from .models import Heading
from .models import Quest

# Create your views here.


def tutor_dash(request):
    return render(request,'tutor/tutor_dashboard.html')

def addcourse(request):
    if request.method == 'GET':
        form = CourseForm()
        return render(request,'tutor/courseform.html',{'form' : form})
    else:
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tutor:newcourse')



def addheading(request):
    if request.method == 'GET':
        form = HeadingForm()
        return render(request,'tutor/headingform.html',{'form' : form})
    else:
        form = HeadingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tutor:newheading')



def addquest(request):
    if request.method == 'GET':
        form = QuestionForm()
        return render(request,'tutor/questionform.html',{'form' : form})
    else:
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tutor:newquest')


def courselist(request):
    course = { 'course_list' : Course.objects.all() }
    return render(request, "tutor/course_list.html", course)


def course_del(request,id):
    course = Course.objects.get(pk=id)
    course.delete()
    return redirect('tutor:courselist')


def course_detail(request,id):
    heading = {'heading_list' : Heading.objects.all().filter(course = id)}
    return render(request,'tutor/course_details.html',heading)


def heading_del(request,id):
    heading = Heading.objects.get(pk=id)
    course_id = heading.course.id
    heading.delete()
    return redirect('tutor:coursedetails',id=course_id)


def heading_detail(request,id):
    question = {'question_list' : Quest.objects.all().filter(heading = id)}
    return render(request,'tutor/heading_details.html',question)


def update_question(request,id):
    question = Quest.objects.get(pk=id)
    form = QuestionForm(instance=question)

    if request.method == 'POST':
        form = QuestionForm(request.POST,instance=question)
        if form.is_valid():
            form.save()
        heading_id  = question.heading.id
        return redirect('tutor:headingdetails',id=heading_id)

    context = {'question':question,'form':form}
    return render(request, 'tutor/questionform.html', context)


def question_del(request,id):
    question = Quest.objects.get(pk=id)
    heading_id  = question.heading.id
    question.delete()
    return redirect('tutor:headingdetails',id=heading_id)