from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from .forms import RegisterForm,UserregisterForm
from.models import Customuser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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


def user_profile(request):
    return render(request,'authenticate/profile.html',{'name':request.user})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form_login=AuthenticationForm(request=request, data=request.POST)
            try:
                if form_login.is_valid():
                    uname=form_login.cleaned_data['username']
                    upass=form_login.cleaned_data['password']
                    user=authenticate(username=uname, password=upass)
                    print(user.is_superuser)
                    if user is not None:
                        if not user.is_superuser and user.customuser.usertype == "Student":
                            print("student")
                            login(request,user,)
                            messages.success(request,'logged in successfully')
                            return HttpResponseRedirect('/studentprofile/')

                        elif not user.is_superuser and user.customuser.usertype == "Faculty":
                            print("faculty")
                            login(request,user)
                            messages.success(request,'logged in successfully')
                            return HttpResponseRedirect('/facultyprofile/')

                        elif user.is_superuser:
                            print("superuser")
                            login(request,user)
                            messages.success(request,'logged in successfully')
                            return HttpResponseRedirect('/profile/')

                        else:
                            print("else")
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


def studentprofile(request):
    return render(request,'authenticate/studentprofile.html',{'name':request.user})

def facultyprofile(request):
    return render(request,'authenticate/facultyprofile.html',{'name':request.user})
