
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import Attendance, Student_Attendance
from Student.models import Student, Subject
from .forms import Attendanceform, Studentattendanceform
from Teacher.models import Teacher
# Create your views here.

def attendance(request):
    if request.method=="POST":
        attendance_form=Attendanceform(request.POST)
        if attendance_form.is_valid():
            attendance = attendance_form.save()
            return redirect(f'/attendance/create_student_attendance/{attendance.id}')
            
    else:
        attendance_form=Attendanceform()
    return render(request,'Attendance/attendance.html',{'form':attendance_form})

def show_attendance(request):
    showdata=Attendance.objects.all()
    return render(request,'Attendance/showattendance.html',{'form':showdata})


def updateattendance(request):
    if request.method=="POST":
        data = request.body.decode('utf-8')
        import json
        data = json.loads(data)
        attendance = Attendance.objects.filter(subject_id=data["subject"], date__date=data["date"])
        print(attendance)
        if attendance and attendance.first():
            return JsonResponse({"attendance":attendance.first().id})
        else:
            print("return")
            return JsonResponse({"detail":"No Attendance for given subject and date."}, safe=False)



    elif request.method=="GET":
        teacher=Teacher.objects.get(access__user=request.user)
        subjects=Subject.objects.filter(subject_teacher=teacher)
        return render(request,'Attendance/updateattendance.html',{'subjects':subjects})



def student_attendance(request):
    if request.method=="POST":
        studentattendance_form=Studentattendanceform(request.POST)
        if studentattendance_form.is_valid():
            studentattendance_form.save()
            studentattendance_form=Studentattendanceform()

    else:
        studentattendance_form=Studentattendanceform()
    return render(request,'Attendance/studentattendance.html',{'form':studentattendance_form})

def create_student_attendance(request, id):
    if request.method=="GET":
        attendance = Attendance.objects.get(id=id)
        students=Student.objects.filter(mapper__student_class=attendance.subject.student_class).distinct()
        return render(request,'Attendance/studentshow.html',{'attendance':attendance, "students":students})
    elif request.method=="POST":
        data = request.body.decode('utf-8')
        import json
        data = json.loads(data)
        student_attendances = []
        for idx, item in enumerate(data.get("students")):
            student_attendance = Student_Attendance(attendance_id=id, student_id=item, is_present=data.get("present")[idx])
            student_attendance.save()
            student_attendances.append(student_attendance)
        return HttpResponse({"students":student_attendance})

def updatestudentattendance(request, id):
    if request.method=="GET":
        attendance = Attendance.objects.get(id=id)
        students=Student_Attendance.objects.filter(attendance=attendance)
        print(students)
        return render(request,'Attendance/studentupdateattendance.html',{'attendance':attendance, "students":students})
    elif request.method=="POST":
        data = request.body.decode('utf-8')
        import json
        data = json.loads(data)
        student_attendances = []
        for idx, item in enumerate(data.get("students")):
            student_attendance = Student_Attendance(attendance_id=id,is_present=data.get("present")[idx])
            student_attendance.save()
            student_attendances.append(student_attendance)
        return HttpResponse({"students":student_attendance})
        return render(request,'Attendance/studentupdateattendance.html',{"data":attendance})
    # write method for post call
    # data to come is studentattendance id and is_present