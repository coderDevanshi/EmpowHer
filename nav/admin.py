from django.contrib import admin
from .models import Profile,User,Community,Course
from django.contrib.auth.admin import Group,UserAdmin

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Community)
admin.site.register(Profile)


