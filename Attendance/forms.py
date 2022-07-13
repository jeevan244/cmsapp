from django import forms
from .models import Attendance, Student_Attendance

class Attendanceform(forms.ModelForm):
    class Meta:
        model=Attendance
        fields='__all__'


class Studentattendanceform(forms.ModelForm):
    class Meta:
        model=Student_Attendance
        fields='__all__'