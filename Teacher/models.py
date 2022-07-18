from django.db import models
from authenticate.models import Customuser

# Create your models here.
class Teacher(models.Model):
    access=models.OneToOneField(Customuser, on_delete=models.CASCADE, related_name='teacher')
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other','Other')
    )
    gender = models.CharField(max_length=6, choices=gender_choices)

    department_choice=(
       ('CSE','Computer Science & Engineering'),
       ('ME','Mechanical Engineering'),
       ('CE','Civil Engineering'),
       ('EE','Electrical Engineering'),
    )

    department = models.CharField(max_length=5, choices=department_choice, default='ME')

    is_HOD = models.BooleanField(default=False)

    phone=models.IntegerField()
    
    

