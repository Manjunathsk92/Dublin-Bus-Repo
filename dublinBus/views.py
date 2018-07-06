from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from dublinBus.models import *
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class UserCreateForm(UserCreationForm):
    #email_field = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username",  "password1", "password2", "email", "first_name", "last_name")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        #user.email_field = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

@login_required(login_url="/")
def about(request):
	return render(request,'about.html',{})

def map_reader(request):
	return render(request, 'busmap.html',{})

def heatmap(request):
    return render(request, 'heatmap.html',{})

def get_routes(request):
    all_routes=list(Routes.objects.values())
    #print(type(all_entries))
    return JsonResponse(all_routes, safe=False)

def signup_view(request):
    if request.method == 'POST':
       form=UserCreateForm(request.POST)
       if form.is_valid():
            form.save()
            user=form.get_user()
            login(request,user)
            return redirect('dublinBus:home_page')
    else:
        form=UserCreateForm()
    return render(request, 'signup.html',{'form': form})

def login_view(request):
    if request.method == 'POST':
       form=AuthenticationForm(data=request.POST)
       if form.is_valid():
           user=form.get_user()
           login(request,user)
           return redirect('dublinBus:home_page')
    else:
        form=AuthenticationForm()
    return render(request, 'login.html',{'form': form})

def logout_view(request):
    logout(request)
    #add logout button using react and check for post method
    return redirect('dublinBus:login')

def test_view(request):
    return render(request, 'test.html',{})

