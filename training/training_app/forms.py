from .models import Courses,sub_Courses
from django import forms

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields =('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
        }

class Sub_Course_Form(forms.ModelForm):
    class Meta:
        model = sub_Courses
        fields = ('name','course','description')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}),
        }