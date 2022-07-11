from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customuser')
    user_choices = (
        ('Student', 'Student'),
        ('Faculty', 'Faculty'),
    )
    usertype= models.CharField(max_length=7, choices=user_choices)

    def __str__(self):
        return self.user.username













