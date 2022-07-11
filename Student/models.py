from django.db import models
from authenticate.models import Customuser
# Create your models here.

class Student(models.Model):
    user_type=models.OneToOneField(Customuser, on_delete=models.CASCADE, related_name='student')
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other','Other')
    )
    gender = models.CharField(max_length=6, choices=gender_choices)

    role_number=models.IntegerField()

    phone=models.IntegerField()

    blood_group=models.CharField(max_length=20)

    def __str__(self):
        return self.user_type.user.username+ " " + str(self.role_number)


class Address(models.Model):
    user_id=models.ForeignKey(Customuser, on_delete=models.CASCADE, related_name='addresses')
    line_1=models.CharField(max_length=200)
    line_2=models.CharField(max_length=200, null=True)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()

    def __str__(self):
        return self.line_1 + self.line_2 + self.city + self.state + str(self.pincode)
    

class Course(models.Model):
    course_title_choice=(
        ('M.Tech','M.Tech'),
        ('B.Tech','B.Tech'),
        ('Diploma','Diploma')
    )
    course_title=models.CharField(max_length=8, choices=course_title_choice, default='B.Tech')


    course_duration_choice=(
        ('4 years','4 years'),
        ('3 years','3 years'),
        ('2 years','2 years')
    )
    course_duration = models.CharField(max_length=8, choices=course_duration_choice, default='4 years')



class Session(models.Model):
    start_year=models.CharField(max_length=6)
    end_year=models.CharField(max_length=8)

    def __str__(self):
        return str(self.start_year)+ "-" + str(self.end_year)


class Class(models.Model):
    department_choice=(
       ('CSE','Computer Science & Engineering'),
       ('ME','Mechanical Engineering'),
       ('CE','Civil Engineering'),
       ('EE','Electrical Engineering'),
    )

    department = models.CharField(max_length=5, choices=department_choice, default='ME')

    course=models.ForeignKey(Course, on_delete=models.CASCADE, related_name='classes')

    session=models.ForeignKey(Session, on_delete=models.CASCADE, related_name='classes')

    year_choice=(
        ('1st year','1st year'),
        ('2nd year','2nd year'),
        ('3rd year','3rd year'),
        ('4th year','4th year'),
    )

    year = models.CharField(max_length=9, choices=year_choice, default ='1st year')

    def __str__(self):
        return f"{self.department} {self.year}"


class Student_class_mapper(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name='mapper')
    student_class=models.ForeignKey(Class, on_delete=models.CASCADE, related_name='mapper')


