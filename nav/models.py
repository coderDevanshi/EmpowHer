from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
  watchlist=models.ManyToManyField('Course', related_name='watchlist', blank=True)
  #blog=models.ForeignKey('Blog',related_name='blogs',on_delete=models.CASCADE ,blank=True)

class Course(models.Model):
  title =models.CharField(max_length=100 , verbose_name="Title")
  description = models.TextField(verbose_name="Description")
  video_link=models.CharField(max_length=11, verbose_name="Video Link")
  created_at=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

class Blog(models.Model):
  title = models.CharField(max_length=100, verbose_name="Title",blank=True,null=True)
  content= models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  like_count = models.IntegerField(default=0)

  def __str__(self):
    return str(self.title)
  
class Watchlist(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_watchlist") #Creates a foreignkey relationship between the WatchList Model and the User model 
  course=models.ForeignKey(Course,on_delete=models.CASCADE ,related_name='course_watchlist')

class Readlist(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  blog=models.ForeignKey(Blog,on_delete=models.CASCADE)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'blog')

    def __str__(self):
        return f"{self.user.username} likes {self.blog.title}"  

class Profile(models.Model):
  branches=[("Computer Science","COMPUTER SCIENCE") , ("Science", "SCIENCE") ,("Commerce" , "COMMERCE") ,("Arts","ARTS"),("All","ALL"),("Other","OTHERS")]
  gender=[("Female" ,"FEMALE"),("Male","MALE"),("Other","OTHERS")]
  degrees=[("BA","BA") ,("BSc","BSc") ,("BCom","BCom") ,("BBA","BBA"),("BBA","BBA") ,("MBA","MBA"),("MSc","MSc"),("MCom","MCom"), ("PhD", "PhD"), ("BTech", "BTECH"), ("Others", "Others")]
  skills = [("Singing", "SINGING"), ("Dancing", "DANCING"), ("Reading", "READING"), ("Writing", "WRITING"), ("Cooking", "COOKING"), ("Sports", "SPORTS"), ("Coding", "CODING"), ("Robotics", "ROBOTICS"), ("Android Development", "ANDROID DEVELOPMENT"), ("Others", "OTHERS")]
  name=models.CharField(max_length=5000,verbose_name="name" ,null=True)
  email=models.EmailField(verbose_name="email", null=  True)
  branch=models.CharField(max_length=5000,choices=branches , blank=True , verbose_name='Branch', null=True)
  degree=models.CharField(max_length=5000,choices=degrees ,null=True , blank=True)
  gender=models.CharField(choices=gender ,verbose_name="Gender" ,max_length=5000, null=True)
  marks_10 = models.IntegerField(verbose_name = "10th Marks", blank=True, null=True)
  marks_12 = models.IntegerField(verbose_name = "12th Marks", blank=True, null=True)
  skill = models.CharField(choices=skills, blank=True, verbose_name = "Skill", max_length=4098, null=True)

  def __str__(self):
    return f"{self.name}'s Profile"

class Jobs(models.Model):
  job_title =models.CharField(max_length=300,verbose_name="job_title")
  link=models.CharField(max_length=300, verbose_name="link")
  source=models.CharField(max_length=300 , verbose_name="source")
  salary_from=models.CharField(max_length=300, verbose_name="salary_from")          
  salary_to=models.CharField(max_length=300, verbose_name="salary_to")         
  salary_currency=models.CharField(max_length=300, verbose_name="salary_currency")
  salary_periodicity=models.CharField(max_length=300, verbose_name="salary_periodicity")
  salary_period=models.CharField(max_length=300, verbose_name="salary_period")
  based_on=models.CharField(max_length=300, verbose_name="based_on")

  '''class Community(models.Model):
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  content=models.TextField()
  created_at=models.DateTimeField(auto_now_add=True)'''