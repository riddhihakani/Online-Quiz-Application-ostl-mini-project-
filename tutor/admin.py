from django.contrib import admin
from .models import Course
from .models import Heading
from .models import Quest

# Register your models here.

admin.site.register(Course)
admin.site.register(Heading)
admin.site.register(Quest)
