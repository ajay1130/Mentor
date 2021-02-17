from django.db import models
from django.db.models import Q
# from django.utils import timezone

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(User,related_name="author_message",on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    filedata = models.FileField(upload_to="uploadedfiles",default="")
    rauthor = models.TextField(default="")

    def __str__(self):
        return self.author.username

    def last_10_messages(author,rauthor):
        # print("hello bro",timezone.now())
        rauthorusername = User.objects.get(username=rauthor)
        # Message.objects.filter(author=author,rauthor=rauthor)
        return Message.objects.filter(Q(author=author,rauthor=str(rauthor)) | Q(author=rauthorusername,rauthor=str(author))).order_by('-timestamp').reverse().all()
        # [:10]
        # .order_by('-timestamp').all()[:10]
 
