from django.urls import path
from .import views

urlpatterns = [
    path('student/',views.student, name='student'),
    path('mapper/',views.mapper, name='mapper'),
    path('address/',views.address, name='address'),
    path('subject/',views.subject, name='subject'),
    path('course/',views.course, name='course'),
    path('session/',views.session, name='session'),
    path('class/',views.studentclass, name='class'),
    path('studentmapper/',views.studentmapper, name='studentmapper'),
    path('showstudent/',views.showstudent,name='showstudent'),
    path('details/<int:my_id>/',views.studentdetails,name='details'),
    path('showsubject/',views.showsubject,name='showsubject'),
    path('showaddress/',views.showaddress,name='showaddress'),
    path('showsession/',views.showsession,name='showsession'),
    path('showcourse/',views.showcourse,name='showcourse'),
    path('showclass/',views.showclass,name='showclass'),
    path('updateaddress/<int:my_id>/',views.updateaddress, name='updateaddress'),
    path('updatecourse/<int:my_id>/',views.updatecourse, name='updatecourse'),
    path('updatesession/<int:my_id>/',views.updatesession, name='updatesession'),
    path('updateclass/<int:my_id>/',views.updateclass, name='updateclass'),
    path('updatestudent/<int:my_id>/',views.updatestudent, name='updatestudent'),
    path('updatesubject/<int:my_id>/',views.updatesubject, name='updatesubject'),
]