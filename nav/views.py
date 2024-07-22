from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User,Profile,Course,Blog,Watchlist,Readlist,Like 
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from .forms import BlogForm,CourseForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse

User=get_user_model()

# Create your views here.
'''class NewCommentForm(ModelForm):
  class Meta:
    model=Comment
    fields=['content']'''

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
    profile=Profile(name,email,gender,branch,degree,skill,marks_10,marks_12)
    profile=Profile(name=name,email=email,gender=gender,branch=branch,degree=degree,skill=skill,marks_10=marks_10,marks_12=marks_12)
    profile.save()

    punctuation="@!#$%^&."
    alphas,nums,lower,upper,special=0,0,0,0,0
    for i in password:
      if i.isalpha():
        alphas+=1
      if i.isnumeric():
        nums+=1
      if i.islower():
        lower+=1
      if i.isupper():
        upper+=1
      if i in punctuation:
        special+=1

    if len(password)<8 or alphas<1 or nums<1 or lower<1 or upper<1 or special<1:
      return render(request,"nav/register.html",{"message":" Password must contain atleast 8 characters, 1 alphabet, 1 number, 1 lowercase, 1 uppercase and 1 special character"})

    if password!=confirmation:   
      return render(request,"nav/register.html",{"message":"Passwords do not match"})
    
    try:
      user=User.objects.create_user(name,email,password)
      user.save()

    except IntegrityError:
       return render(request,"nav/register.html",{"message":"User already exists"})
    login(request,user)
    return render(request,"nav/register.html",{"message":"User registered successfully"}) 

  else:
    return render(request,"nav/register.html")

def login_view(request):
  if request.method=="POST":
    name=request.POST["name"]
    password=request.POST["password"]
    user=authenticate(request,username=name,password=password)

    if user is not None:
      login(request,user) #Log the user in
      return render(request,"nav/home.html",{"message" : "Logged"}) #Redirect to home page or another view(later on change)
    
    else:
      return render(request,'nav/login.html',{'message':"Invalid credentials"})
    
  else:
    return render(request,'nav/login.html') 

def logout_view(request):
  logout(request)

  return render(request,"nav/home.html") #(Just for now)#return HttpResponseRedirect(reverse("landing"))

def blog_list(request):
  blogs=Blog.objects.all().order_by('created_at')
  return render(request,"nav/blog_list.html" ,{"blogs":blogs})

@login_required
def blog_create(request):
  if request.method=='POST':
    form=BlogForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('blog_list')
  else:
    form=BlogForm()  #If request is GET then an empty form is displayed for the user to fill out

  return render(request,'nav/blog_form.html',{'form':form})  

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'nav/blog_detail.html', {'blog': blog})

@login_required
def blog_delete(request, blog_id):
  blog=get_object_or_404(Blog, pk=blog_id)
  blog.delete()
  return redirect('blog_list')


@login_required
def blog_update(request,blog_id):
  blog=get_object_or_404(Blog,pk=blog_id)
  
  if(request.method=='POST'):
    form=BlogForm(request.POST,instance=blog) #instance is used to update the existing blog
    if(form.is_valid()):
       form.save()
       return redirect('blog_detail',blog_id=blog_id)

  else:
      form=BlogForm(instance=blog)
  
  return render(request,'nav/blog_form.html',{'form':form})   

@staff_member_required 
def course_create(request):
  if request.method=='POST':
    form=CourseForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('course_list') #We always redirect to a url/path name not the actual path and render to the actual path or html page
  else:
    form=CourseForm()
  return render(request, 'nav/course_form.html',{'form':form}) 

def course_list(request):
  courses=Course.objects.all()
  return render(request,'nav/course_list.html',{'courses':courses})

def course_detail(request,course_id):
  course=get_object_or_404(Course ,pk=course_id)
  
  return render(request,'nav/course_detail.html',{'course':course})

def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.like_count += 1
    blog.save()
    return JsonResponse({'like_count': blog.like_count})

@login_required
def add_to_watchlist(request,course_id):
  course=get_object_or_404(Course, id=course_id)

  Watchlist.objects.get_or_create(user=request.user,course=course) #get_or_create is a method that returns an object if it exists or creates a new object if it does not exist .In Watchlist.objects.create(user=request.user,course=course) watchlist is the model name and user and course are the fields in the model the working is as follows 

  return redirect('watchlist')

@login_required
def watchlist(request):
  watchlist_courses=Watchlist.objects.filter(user=request.user)
  return render(request, 'nav/watchlist.html', {'watchlist_courses': watchlist_courses})

@login_required
def add_to_readlist(request,blog_id):
  blog=get_object_or_404(Blog,id=blog_id)
  Readlist.objects.get_or_create(user=request.user,blog=blog)
  return redirect('readlist')

@login_required
def readlist(request):
  readlist_blogs=Readlist.objects.filter(user=request.user)
  return render(request,'nav/readlist.html',{'readlist_blogs':readlist_blogs})

@login_required
def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    user = request.user

    # Check if the user has already liked the blog
    if Like.objects.filter(user=user, blog=blog).exists():
        return JsonResponse({'message': 'You have already liked this blog.'}, status=400)

    # Create a new like
    Like.objects.create(user=user, blog=blog)
    blog.like_count += 1
    blog.save()

    return JsonResponse({'like_count': blog.like_count})
