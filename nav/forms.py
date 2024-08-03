from django import forms
from .models import Blog,Course,Resume

class BlogForm(forms.ModelForm):
  class Meta:
    model=Blog
    fields=['title','content']

class CourseForm(forms.ModelForm):
  class Meta:
    model=Course
    fields=['title','description','video_link']

class ResumeForm(forms.ModelForm):
  class Meta:
    model=Resume
    fields=['document']
