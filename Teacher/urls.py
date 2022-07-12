from django.urls import path
from .import views

urlpatterns = [
    path('teacher/',views.teacher, name="teacher"),
    path('showteacher/',views.showteacher, name="showteacher"),
    path('updateteacher/<int:my_id>/',views.updateteacher, name='updateteacher'),
]