from django.db import models
from django.contrib.auth.models import User
from django.db.models import DO_NOTHING
from django.conf import settings

# Create your models here.

PROFESSION = (

    ('Student','student'),
    ('Housewife','housewife'),
    ('Businessman','businessman'),   
    ('other','other'),
)

DEGREES = (
    ('POST GRADUATE','postgraduate'),
    ('GRADUATE','graduate'),
    ('10th pass','10thpass'),
    ('12th pass','12thpass'),
)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    profession = models.CharField('Profession',choices=PROFESSION,max_length=12)
    degree = models.CharField('Degree',choices=DEGREES,max_length=18)
    state = models.CharField(max_length=30)
    nationality = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    profile_img = models.ImageField(default='default.jpg',blank=True)
    bio = models.TextField()