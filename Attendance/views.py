from django.shortcuts import render
from .models import Attendance, Student_Attendance
from .forms import Attendanceform, Studentattendanceform
# Create your views here.

def attendance(request):
    if request.method=="POST":
        attendance_form=Attendanceform(request.POST)
        if attendance_form.is_valid():
            attendance_form.save()
            attendance_form=Attendanceform()

    else:
        attendance_form=Attendanceform()
    return render(request,'Attendance/attendance.html',{'form':attendance_form})

def show_attendance(request):
    showdata=Attendance.objects.all()
    return render(request,'Attendance/showattendance.html',{'form':showdata})


def updateattendance(request,my_id):
    if request.method=="POST":
        update_attendance=Attendance.objects.get(pk=my_id)
        update_form=Attendanceform(request.POST,instance=update_attendance)
        if update_form.is_valid():
            update_attendance=update_form.save(commit=False)
            update_attendance=update_form.save()
            return HttpResponseRedirect('/attendance/showattendance')

    else:
        update_attendance=Attendance.objects.get(pk=my_id)
        update_form=Attendanceform(instance=update_attendance)
    return render(request,'Attendance/updateattendance.html',{'form':update_form})



def student_attendance(request):
    if request.method=="POST":
        studentattendance_form=Studentattendanceform(request.POST)
        if studentattendance_form.is_valid():
            studentattendance_form.save()
            studentattendance_form=Studentattendanceform()

    else:
        studentattendance_form=Studentattendanceform()
    return render(request,'Attendance/studentattendance.html',{'form':studentattendance_form})

def show_student_attendance(request):
    showdata=Student_Attendance.objects.all()
    return render(request,'Attendance/studentshow.html',{'form':showdata})