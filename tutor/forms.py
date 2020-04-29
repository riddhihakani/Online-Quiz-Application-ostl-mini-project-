from django import forms
from .models import Course
from .models import Heading
from .models import Quest



class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = ('coursename','coursedescription')
        labels = {
            'coursename' : 'Course Name',
            'coursedescription' : 'Description',
        }



class HeadingForm(forms.ModelForm):
    
    class Meta:
        model = Heading
        fields = ('course','headingname','difficultylevel','headingdescription','time','code')
        labels = {
            'course' : 'Course',
            'headingname' : 'Topic',
            'difficultylevel' : 'Difficulty Level',
            'headingdescription' : 'Description',
            'time' : 'Time Limit',
        }

    def __init__(self, *args, **kwargs):
        super(HeadingForm,self).__init__(*args, **kwargs)
        self.fields['course'].empty_label = "Select"



class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Quest
        fields = ('heading','FullQuestion','option1','option2','option3','option4','answer','marks')
        labels = {
            
            'heading' : 'Topic',
            'option1' : 'Option 1',
            'option2' : 'Option 2',
            'option3' : 'Option 3',
            'option4' : 'Option 4',
            'FullQuestion' : 'Question',
            'answer'       : 'Correct Answer',
            'marks'        : 'Points',
        }

    def __init__(self, *args, **kwargs):
        super(QuestionForm,self).__init__(*args, **kwargs)
        self.fields['heading'].empty_label = "Select"
        
        
