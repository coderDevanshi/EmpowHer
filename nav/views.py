from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User,Profile,Community,Blog,Course

# Create your views here.

def register(request):
  if request.method=='POST':

    name=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']
    confirmation=request.POST['confirmation']
    branch=request.POST['branch']
    degree=request.POST['degree']
    gender=request.POST['gender']
    marks_10=request.POST['marks_10']
    marks_12=request.POST['marks_12']
    skill=request.POST['skill']
    profile=Profile(name=name,email=email,password=password,confirmation=confirmation,branch=branch,)


    
