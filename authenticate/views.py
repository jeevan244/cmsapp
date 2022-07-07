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
        custom_user_form=UserregisterForm(request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user_form=RegisterForm()
            
                     
    else:
        user_form=RegisterForm()
    return render(request,'authenticate/register.html',{'form':user_form})


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
                        login(request,user)
                        messages.success(request,'logged in successfully')
                        return HttpResponseRedirect('/profile/')

                else:
                    return HttpResponse({"please provide correct username and password !!!!"})
            except Exception as e:
                return HttpResponse({"error":e})
        else:
            form_login=AuthenticationForm()
            return render(request,'authenticate/login.html',{'form':form_login})
    else:
        return HttpResponseRedirect('/profile/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def user_profile(request):
    return render(request,'authenticate/profile.html',{'name':request.user})