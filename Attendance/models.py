from django.db import models
from Student.models import Student, Subject
from datetime import datetime

# Create your models here.
class Attendance(models.Model):
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subjects')
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.date)



class Student_Attendance(models.Model):
    attendance=models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name='studentattendance')
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name='learner')
    is_present=models.BooleanField(default=False)   