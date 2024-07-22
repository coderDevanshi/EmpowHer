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
  path('course_list/',views.course_list,name='course_list'),
  path('course_create/',views.course_create,name='course_create'),
  path('courses/<int:course_id>/',views.course_detail , name='course_detail'),
  path('blog/<int:blog_id>/like/', views.like_blog, name='like_blog'),
  path('add_to_watchlist/<int:course_id>/', views.add_to_watchlist, name='add_to_watchlist'),
  path('watchlist/', views.watchlist, name='watchlist'),
  path('add_to_readlist/<int:blog_id>/', views.add_to_readlist, name='add_to_readlist'),
  path('readlist/', views.readlist, name='readlist'),
]