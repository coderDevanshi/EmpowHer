from django import forms
from .models import Blog,Course

class BlogForm(forms.ModelForm):
  class Meta:
    model=Blog
    fields=['title','content']

class CourseForm(forms.ModelForm):
  class Meta:
    model=Course
    fields=['title','description','video_link']