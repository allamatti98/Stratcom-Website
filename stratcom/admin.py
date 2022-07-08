from django.contrib import admin
from .models import User
from .models import UserProfile

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','name','institution','contact','program')

admin.site.register(User,UserAdmin)
admin.site.register(UserProfile)