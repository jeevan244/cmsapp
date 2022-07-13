from django.db import models
from Student.models import Student, Subject
from datetime import datetime

# Create your models here.
class Attendance(models.Model):
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateTimeField(default=datetime.now, blank=True)



class Student_Attendance(models.Model):
    attendance=models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name='studentattendance')
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name='studentattendance')
    is_present=models.BooleanField(default=True)