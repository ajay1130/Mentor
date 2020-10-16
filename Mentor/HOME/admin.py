from django.contrib import admin
from HOME.models import Contact
from HOME.models import Profile,ToDoListData
# from HOME.models import ToDoList
# Register your models here.
admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(ToDoListData)

