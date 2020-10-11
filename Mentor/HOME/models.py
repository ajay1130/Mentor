from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    date = models.DateField()