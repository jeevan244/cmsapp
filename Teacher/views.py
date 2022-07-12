from django.shortcuts import render
from .models import Teacher
from .forms import Teacherform
# Create your views here.

def teacher(request):
    if request.method=="POST":
        teacher_form=Teacherform(request.POST)
        if teacher_form.is_valid():
            teacher_form.save()
            teacher_form=Teacherform()

    else:
        teacher_form=Teacherform()
    return render(request,'Teacher/teacher.html',{'form':teacher_form})
    

def showteacher(request):
    showdata=Teacher.objects.all()
    return render(request,'Teacher/showteacher.html',{'form':showdata})


def updateteacher(request,my_id):
    if request.method=="POST":
        update_teacher=Teacher.objects.get(pk=my_id)
        update_form=Teacherform(request.POST,instance=update_teacher)
        if update_form.is_valid():
            update_teacher=update_form.save(commit=False)
            update_teacher=update_form.save()
            return HttpResponseRedirect('/teacherpath/showteacher')

    else:
        update_teacher=Teacher.objects.get(pk=my_id)
        update_form=Teacherform(instance=update_student)
    return render(request,'Teacher/updateteacher.html',{'form':update_form})
