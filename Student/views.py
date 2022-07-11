from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import Studentform,Addressform,Courseform,Sessionform,Classform
from .models import Student,Address,Course,Session,Class
from django.contrib import messages
# Create your views here.

def student(request):
    if request.method=="POST":
        student_form=Studentform(request.POST)
        if student_form.is_valid():
            student_form.save()
            student_form=Studentform()

    else:
        student_form=Studentform()
    return render(request,'Student/student.html',{'form':student_form})

def showstudent(request):
    showdata=Student.objects.all()
    return render(request,'Student/showstudent.html',{'form':showdata})


def updatestudent(request,my_id):
    if request.method=="POST":
        update_student=Student.objects.get(pk=my_id)
        update_form=Studentform(request.POST,instance=update_student)
        if update_form.is_valid():
            update_student=update_form.save(commit=False)
            update_student=update_form.save()
            return HttpResponseRedirect('/studentpath/showstudent')

    else:
        update_student=Student.objects.get(pk=my_id)
        update_form=Studentform(instance=update_student)
    return render(request,'Student/updatestudent.html',{'form':update_form})


def address(request):
    if request.method=="POST":
        address_form=Addressform(request.POST)
        if address_form.is_valid():
            address_form.save()
            address_form=Addressform()

    else:
        address_form=Addressform()
    return render(request,'Student/address.html',{'form':address_form,'data':showdata})

def showaddress(request):
    showdata=Address.objects.all()
    return render(request,'Student/showaddress.html',{'form':showdata})


def updateaddress(request,my_id):
    if request.method=="POST":
        update_address=Address.objects.get(pk=my_id)
        update_form=Addressform(request.POST,instance=update_address)
        if update_form.is_valid():
            update_address=update_form.save(commit=False)
            update_address=update_form.save()
            return HttpResponseRedirect('/studentpath/showaddress')

    else:
        update_address=Address.objects.get(pk=my_id)
        update_form=Addressform(instance=update_address)
    return render(request,'Student/updateaddress.html',{'form':update_form})


def course(request):
    if request.method=="POST":
        course_form=Courseform(request.POST)
        if course_form.is_valid():
            course_form.save()
            course_form=Courseform()
    else:
        course_form=Courseform()
    return render(request,'Student/course.html',{'form':course_form, 'data':show_data})


def showcourse(request):
    showdata=Course.objects.all()
    return render(request,'Student/showcourse.html',{'form':showdata})


def updatecourse(request,my_id):
    if request.method=="POST":
        update_course=Course.objects.get(pk=my_id)
        update_form=Courseform(request.POST,instance=update_course)
        if update_form.is_valid():
            update_course=update_form.save(commit=False)
            update_course=update_form.save()
            return HttpResponseRedirect('/studentpath/showcourse')

    else:
        update_course=Course.objects.get(pk=my_id)
        update_form=Courseform(instance=update_course)
    return render(request,'Student/updatecourse.html',{'form':update_form})



def session(request):
    if request.method=='POST':
        session_form=Sessionform(request.POST)
        if session_form.is_valid():
            session_form.save()
            session_form=Sessionform()

    else:
        session_form=Sessionform()
    return render(request,'Student/session.html',{'form':session_form, 'data':show_data})

def showsession(request):
    showdata=Session.objects.all()
    return render(request,'Student/showsession.html',{'form':showdata})


def updatesession(request,my_id):
    if request.method=="POST":
        update_session=Session.objects.get(pk=my_id)
        update_form=Sessionform(request.POST,instance=update_session)
        if update_form.is_valid():
            update_session=update_form.save(commit=False)
            update_session=update_form.save()
            return HttpResponseRedirect('/studentpath/showsession')

    else:
        update_session=Session.objects.get(pk=my_id)
        update_form=Sessionform(instance=update_session)
    return render(request,'Student/updatesession.html',{'form':update_form})


def studentclass(request):
    if request.method=="POST":
        class_form=Classform(request.POST)
        if class_form.is_valid():
            class_form.save()
            class_form=Classform()
    else:
        class_form=Classform()
    show_data=Class.objects.all()
    return render(request,'Student/class.html',{'form':class_form, 'data':show_data})

def showclass(request):
    showdata=Class.objects.all()
    return render(request,'Student/showclass.html',{'form':showdata})

def updateclass(request,my_id):
        if request.method=="POST":
            update_class=Class.objects.get(pk=my_id)
            update_form=Classform(request.POST,instance=update_class)
            if update_form.is_valid():
                update_class=update_form.save(commit=False)
                update_class=update_form.save()
                return HttpResponseRedirect('/studentpath/showclass')

        else:
            update_class=Class.objects.get(pk=my_id)
            update_form=Classform(instance=update_class)
        return render(request,'Student/updateclass.html',{'form':update_form})
