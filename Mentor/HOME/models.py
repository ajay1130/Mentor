from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    gender=models.CharField(max_length=50)
    sem=models.CharField(max_length=20)
    # dob = models.DateField()
    aboutyourself = models.TextField(default="")
    college = models.CharField(max_length=200,default="")
    image = models.ImageField(default='default.png', upload_to="profile_pics")
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    

class ToDoListData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default="")
    task=models.CharField(max_length=200,default="")

    def __str__(self):
        return f'{self.user.username} ToDoList'
        
    