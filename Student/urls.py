from django.urls import path
from .import views

urlpatterns = [
    path('student/',views.student, name='student'),
    path('address/',views.address, name='address'),
    path('course/',views.course, name='course'),
    path('session/',views.session, name='session'),
    path('class/',views.studentclass, name='class'),
    path('updateaddress/<int:my_id>/',views.updateaddress, name='updateaddress'),
    path('updatecourse/<int:my_id>/',views.updatecourse, name='updatecourse'),
    path('updatesession/<int:my_id>/',views.updatesession, name='updatesession'),
    path('updateclass/<int:my_id>/',views.updateclass, name='updateclass'),
    path('updatestudent/<int:my_id>/',views.updatestudent, name='updatestudent'),
]