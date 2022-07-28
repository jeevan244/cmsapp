from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from .forms import RegisterForm,UserregisterForm
from.models import Customuser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Teacher.models import Teacher
from Student.models import Student
# Create your views here.

 
def register(request):
    if request.method=="POST":
        user_form=RegisterForm(request.POST)
        custom_form=UserregisterForm(request.POST)
        if user_form.is_valid and custom_form.is_valid():
            user=user_form.save()
            customuser=custom_form.save(commit=False)
            customuser.user=user
            customuser.save()
            user_form=RegisterForm()
            return HttpResponse({"success"})
                             
    else:
        user_form=RegisterForm()
        custom_form=UserregisterForm()
    return render(request,'authenticate/register.html',{'form':user_form, 'customform':custom_form})


def show_register_user(request):
    show_data=Customuser.objects.all()
    return render(request,'authenticate/showregisteruser.html',{'data':show_data})

def delete(request,my_id):
    delete_data=Customuser.objects.get(id=my_id)
    delete_data.delete()
    return HttpResponseRedirect('/register')


def update(request,my_id):
    data = Customser.objects.get(pk=my_id)
    update_user = UserregisterForm(request.POST, instance= data)
    if update_user.is_valid():
        data = update_user.save(commit=False)
        data= update_user.save()
        return HttpResponseRedirect('/register')

    return render (request, 'authenticate/updateuser.html', {'update_user':update_user})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def user_profile(request,id):
    user=User.objects.get(id=id)
    return render(request,'authenticate/profile.html',{'user':user})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form_login=AuthenticationForm(request=request, data=request.POST)
            try:
                if form_login.is_valid():
                    uname=form_login.cleaned_data['username']
                    upass=form_login.cleaned_data['password']
                    user=authenticate(username=uname, password=upass)
                    if user is not None:
                        if not user.is_superuser and user.customuser.usertype == "Student":
                            login(request,user,)
                            student=Student.objects.get(user_type__user__id=user.id)
                            messages.success(request,'logged in successfully')
                            return HttpResponseRedirect(f'/studentprofile/{student.id}')

                        elif not user.is_superuser and user.customuser.usertype == "Faculty":
                            login(request,user)
                            teacher=Teacher.objects.get(access__user__id=user.id)
                            # print(teacher.id)
                            messages.success(request,'logged in successfully')
                            return HttpResponseRedirect(f'/facultyprofile/{teacher.id}')

                        elif user.is_superuser:
                            login(request,user)
                            user=User.objects.get(id=user.id)
                            # user=User.objects.filter(is_superuser=True).values_list('id')
                            # print(user.id)
                            messages.success(request,'logged in successfully')
                            return HttpResponseRedirect(f'/profile/{user.id}')

                        else:
                            return HttpResponse({"please signup first"})

                else:
                    return HttpResponse({"please provide correct username and password !!!!"})
            except Exception as e:
                print("error ->",e)
                return HttpResponse({"error":e})
        else:
            form_login=AuthenticationForm()
            return render(request,'authenticate/login.html',{'form':form_login})
    else:
        return HttpResponseRedirect('/profile/')


def studentprofile(request, id):
    student=Student.objects.get(id=id)
    return render(request,'authenticate/studentprofile.html',{'student':student})

def facultyprofile(request, id):
    teacher=Teacher.objects.get(id=id)
    print(teacher)
    return render(request,'authenticate/facultyprofile.html',{'teacher':teacher})
