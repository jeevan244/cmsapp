from django import forms
from authenticate.forms import UserregisterForm
from .models import Student, Address, Course, Session, Class, Student_class_mapper, Subject

class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields= '__all__'

class Addressform(forms.ModelForm):
    class Meta:
        model=Address
        fields= '__all__'




class Courseform(forms.ModelForm):
    class Meta:
        model=Course
        fields= '__all__'


class Sessionform(forms.ModelForm):
    class Meta:
        model=Session
        fields= '__all__'


class Classform(forms.ModelForm):
    class Meta:
        model= Class
        fields= '__all__'


class Studentmapper(forms.ModelForm):
    class Meta:
        model=Student_class_mapper
        fields= '__all__'

class Subjectform(forms.ModelForm):
    class Meta:
        model=Subject
        fields= '__all__'