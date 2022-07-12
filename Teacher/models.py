from django.db import models

# Create your models here.
class Teacher(models.Model):
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

    phone=models.IntegerField()
    
    

