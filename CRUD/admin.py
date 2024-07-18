from django.contrib import admin
from .models import user_information
# Register your models here.
@admin.register(user_information)
class userModelAdmin(admin.ModelAdmin):
    list_display = ['name','email','Age','gender','country']