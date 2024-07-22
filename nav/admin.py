from django.contrib import admin
from .models import Profile,User,Course,Blog,Jobs   #Community,
from django.contrib.auth.admin import Group,UserAdmin

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
#admin.site.register(Community)
admin.site.register(Profile)
admin.site.register(Blog)
admin.site.register(Jobs)

