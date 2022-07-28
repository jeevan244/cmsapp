from django.urls import path
from .import views

urlpatterns = [
    path('attendance/',views.attendance, name='attendance'),
    path('showattendance/',views.show_attendance, name='showattendance'),
    path('studentattendance/',views.student_attendance, name='studentattendance'),
    path('create_student_attendance/<int:id>/',views.create_student_attendance, name='showstudentattendance'),
    path('update_student_attendance/',views.updateattendance, name='updateattendance'),
    path('studentupdateattendance/<int:id>/',views.updatestudentattendance, name='updatestudentupdateattendance'),
]