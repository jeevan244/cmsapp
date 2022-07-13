from django.urls import path
from .import views

urlpatterns = [
    path('attendance/',views.attendance, name='attendance'),
    path('showattendance/',views.show_attendance, name='showattendance'),
    path('studentattendance/',views.student_attendance, name='studentattendance'),
    path('showstudentattendance/',views.show_student_attendance, name='showstudentattendance'),
    path('updateattendance/<int:my_id>/',views.updateattendance, name='updateattendance'),
]