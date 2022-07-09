from django.contrib import admin
from .models import User
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username','name','institution','number','program')

admin.site.register(User,CustomUserAdmin)
admin.site.register(UserProfile)