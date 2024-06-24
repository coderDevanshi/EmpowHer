from django.urls import path
from . import views
from django.contrib import admin


urlpatterns=[
  path('register',views.register,name="register"),
  path('login/',views.login_view,name="login_view"),
  #path('', views.home, name='home')
  path('',views.blog_list ,name='blog_list'),
  path('create/',views.blog_create,name='blog_create'),
  path('delete/<int:blog_id>/',views.blog_delete,name='blog_delete'),
  path('update/<int:blog_id>/',views.blog_update,name='blog_update'),
  path('blog_detail/<int:blog_id>/',views.blog_detail,name='blog_detail')
]