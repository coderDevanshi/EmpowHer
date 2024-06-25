from django.urls import path
from . import views
from django.contrib import admin


urlpatterns=[
  path('register',views.register,name="register"),
  path('login/',views.login_view,name="login_view"),
  #path('', views.home, name='home')
  path('blog_list/',views.blog_list ,name='blog_list'),
  path('blog_create/',views.blog_create,name='blog_create'),
  path('blog_delete/<int:blog_id>/',views.blog_delete,name='blog_delete'),
  path('blog_update/<int:blog_id>/',views.blog_update,name='blog_update'),
  path('blog_detail/<int:blog_id>/',views.blog_detail,name='blog_detail'),
  path('courses/',views.course_list,name='course_list'),
  path('courses/create/',views.course_create,name='course_create'),
  path('courses/<int:course_id>/',views.course_detail , name='course_detail'),
]