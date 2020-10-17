from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from datetime import datetime
from HOME.models import Contact,Profile,ToDoListData
from django.contrib.auth import logout
import time
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm

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

def logoutUser(request):
    logout(request)
    return redirect('/')

def contact(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Subject = request.POST.get('Subject')
        message = request.POST.get('message')
        contact = Contact(name=Name,email=Email,subject=Subject,message=message,date=datetime.today())
        contact.save()
        messages.success(request, "You've successfully send messages...")
    return render(request,'contact.html')

@login_required(login_url='/login')
def user(request):
    isNullProfile(request)
    # if request.user.is_anonymous:
    #     return redirect('/')
    if request.method == "POST":
        taskname = request.POST.get('taskname')
        # print(taskname)
        # user = User.objects.get(id=request.user.id)
        # ToDoListData.objects.create(user=user,task=taskname)

    return render(request,'user/index.html')

def isNullProfile(request):
    #  profiledata = Profile.objects.get(user=request.user.id)
    #  print(request.user.username)
    pass
    #  if profiledata.status==False:
    #      return render(request,"user/userprofile.html")

@login_required(login_url='/login')
def messagesuser(request):
    isNullProfile(request)
    return render(request,'user/messages.html')

@login_required(login_url='/login')
def userprofile(request):
    if request.method == "POST":
        # print(request.FILES)

        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        college = request.POST.get('collegename')
        semester = request.POST.get('semester')
        course = request.POST.get('course')
        gender = request.POST.get('gender')
        status = request.POST.get('status')

        user = User.objects.get(id=request.user.id)
        user.first_name =firstname
        user.last_name=lastname
        user.save()

        print(type(status),status)
        if status =="":
            img=""
            if "userimage" in request.FILES:
                img = request.FILES["userimage"]
            # profiledata.image = img
            # profiledata.save()
            if not img=="":
                Profile.objects.create(user=user,course=course,gender=gender,sem=semester,aboutyourself=bio,college=college,image=img,status=True)
            else:
                Profile.objects.create(user=user,course=course,gender=gender,sem=semester,aboutyourself=bio,college=college,status=True)
        else:
            profiledata = Profile.objects.get(user=request.user.id)
            profiledata.college=college
            profiledata.aboutyourself=bio
            profiledata.course=course
            profiledata.gender=gender
            profiledata.sem=semester
            profiledata.status=True
            profiledata.save()
            if "userimage" in request.FILES:
                img = request.FILES["userimage"]
                profiledata.image = img
                profiledata.save()
        
        context={}
        context["msg"]="Your Profile is Updated Successfully!!!!"
        context['col']="alert-success"
        return render(request,'user/userprofile.html',context)

    return render(request,'user/userprofile.html')

def room(request,room_name):
    return render(request, 'user/chat/chatroom.html', {
        'room_name': room_name
    })
@login_required(login_url='/login')
def changepassword(request):
    isNullProfile(request)
    # fm = PasswordChangeForm(user=request.user)
    context={}
    if request.method == "POST":
        oldpwd = request.POST.get('oldpwd')
        newpwd = request.POST.get('newpwd')
        # renewpwd = request.POST.get('renewpwd')

        user = User.objects.get(id=request.user.id)
        check = user.check_password(oldpwd)
        un=user.username
        if check==True:
            user.set_password(newpwd)
            user.save()
            context["msg"]="Password changed successfully!!!"
            context['col']="alert-success"
            user=User.objects.get(username=un)
            login(request,user)
            
        else:
            context["msg"]="Your current password is incorrect"
            context['col']="alert-danger"
            
    return render(request,'user/changepassword.html',context)

def chat(request):
    isNullProfile(request)
    return render(request,'user/chat/index.html',{})

@login_required(login_url='/login')
def notifications(request):
    isNullProfile(request)
    return render(request,'user/notifications.html')

@login_required(login_url='/login')
def profile(request):
    return render(request,'user/otheruserprofile.html')

@login_required(login_url='/login')
def followers(request):
    return render(request,'user/followers.html')


@login_required(login_url='/login')
def following(request):
    return render(request,'user/following.html')

def loginUser(request):
     if request.method == "POST":
        Password = request.POST.get('Password')
        Email = request.POST.get('Email')
        if not User.objects.filter(email=Email).exists():
            context = {"successcode":"User id or password are incorrect !!!" }
            return render(request,'login.html',context)
        Username = User.objects.get(email=Email.lower()).username
        user = authenticate(username=Username, password=Password)
        if user is not None:
            login(request,user)
            return redirect("/user")
        else:
            context = {"successcode":"User id or password are incorrect !!!" }
            return render(request,'login.html',context)
    
     return render(request,'login.html')
    

def register(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        if User.objects.filter(username=username).exists():
            context = {"successcode":"Username is already exists please choose another" }
            return render(request,'login.html',context)
        if User.objects.filter(email=Email).exists():
            context = {"successcode":"Email id is already exists" }
            return render(request,'login.html',context)
        user = User.objects.create_user(username, Email, Password)
        # messages.success(request, "you've successfully registered please try to login...")
        if user is not None:
            context = {"successcode":"You've Successfully Registered Please try to login" }
            # messages.info(request,"You've successfully registerd....")
            return render(request,'login.html',context)
        else:
            context = {"successcode":"There was some problem please try again later" }
            return render(request,'login.html',context)
    else:
        context = {"successcode":"There was some problem please try again later" }
        # return HttpResponse('There was some problem please try again later')
        return render(request,'login.html')   

   
    


