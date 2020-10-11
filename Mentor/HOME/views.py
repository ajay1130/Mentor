from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from datetime import datetime
from HOME.models import Contact

# Create your views here.
def index(request):
    context = {
        "name":"ajay"
    }
    return render(request,'index.html',context)

def about(request):
    context = {
        "name":"ajay"
    }
    return render(request,'about.html',context)

def contact(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Subject = request.POST.get('Subject')
        message = request.POST.get('message')
        contact = Contact(name=Name,email=Email,subject=Subject,message=message,date=datetime.today())
        contact.save()
    return render(request,'contact.html')

def user(request):
    return render(request,'user/index.html')

def messages(request):
    return render(request,'user/messages.html')


def chat(request):
    return render(request,'user/chat.html')

def userprofile(request):
    return render(request,'user/userprofile.html')

def demoChat(request):
    return render(request,'user/demochat.html')

def changepassword(request):
    return render(request,'user/changepassword.html')

def notifications(request):
    return render(request,'user/notifications.html')

def login(request):
     if request.method == "POST":
        Password = request.POST.get('Password')
        Email = request.POST.get('Email')
        Username = User.objects.get(email=Email.lower()).username
        user = authenticate(username=Username, password=Password)
        if user is not None:
            return redirect("/")
        else:
            return render(request,'login.html')
    
     return render(request,'login.html')
    

def register(request):
    if request.method == "POST":
        Username = request.POST.get('Username')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        user = User.objects.create_user(Username, Email, Password)
    if user is not None:
        # messages.info(request,"You've successfully registerd....")
        return redirect("/")
    else:
        # return HttpResponse('There was some problem please try again later')
        return render(request,'login.html')
    


