from django.db import models
from django.contrib.auth.models import User
from django.db.models import DO_NOTHING

# Create your models here.
class Course(models.Model):
    coursename = models.CharField(max_length=50)
    coursedescription = models.TextField()
   

    def __str__(self):
        return self.coursename

DIFFICULTY = (
    ('Beginner','BEGINNER'),
    ('Easy','EASY'),
    ('Medium','MEDIUM'),
    ('Hard','HARD'),
)

class Heading(models.Model):
    headingname = models.CharField(max_length=50)
    difficultylevel = models.CharField('Difficulty Level',choices=DIFFICULTY,max_length=12)
    headingdescription = models.TextField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE,default=None)
    time = models.IntegerField(blank=True,null=True)
    code = models.CharField(max_length=6,default=000000)
    def __str__(self):
        return self.headingname


class Quest(models.Model):
    FullQuestion = models.CharField(max_length=100)
    option1 = models.CharField(max_length=30)
    option2 = models.CharField(max_length=30)
    option3 = models.CharField(max_length=30)
    option4 = models.CharField(max_length=30)
    answer = models.CharField(max_length=30)
    heading = models.ForeignKey(Heading,on_delete=models.CASCADE,default=None)
    marks  = models.IntegerField(default=0)


    def __str__(self):
        return self.FullQuestion




    
    