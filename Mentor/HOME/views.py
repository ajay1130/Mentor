from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from datetime import datetime,date
from .models import *
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
    if not isNullProfile(request):
        return redirect("/userprofile")
    user = User.objects.get(id=request.user.id)
    tasks = ToDoListData.objects.filter(user=user)
    followingcount = FollowersandFollowing.objects.filter(username=request.user).exclude(following="").count()
    followerscount = FollowersandFollowing.objects.filter(username=request.user).exclude(followers="").count()

    todayfollowers = FollowersandFollowing.objects.filter(username=user.id,created=date.today()).exclude(followers="").count()
    # for item in todayfollowers:
    #     print(item.created)
    print("hello")
    context = {'tasks':tasks,'followerscount':followerscount,'followingcount':followingcount,'todayfollowers':todayfollowers}
    # if request.user.is_anonymous:
    #     return redirect('/')
    if request.method == "POST":
        taskname = request.POST.get('taskname')
        user = User.objects.get(id=request.user.id)
        taskdata = ToDoListData(user=user,title=taskname)
        taskdata.save()
        context["msg"]="Your data has been added to  To-Do List...."
        return render(request,'user/index.html',context)
        # print(taskname)
        # user = User.objects.get(id=request.user.id)
        # ToDoListData.objects.create(user=user,task=taskname)

    return render(request,'user/index.html',context)

def isNullProfile(request):
    user = User.objects.get(id=request.user.id)
    if user.first_name=="":
        return False
    return True

def forgetpassword(request):
    context={}
    return render(request,'user/forgetpassword.html',context)

@login_required(login_url='/login')
def messagesuser(request):
    if not isNullProfile(request):
        return redirect("/userprofile")
    if request.method == "POST":
        isFollowing = request.POST.get('isFollowing')
        id = request.POST.get('id')
    # if 'username' in request.session:
    #     del request.session['username']
    user = User.objects.get(id=request.user.id)
    todayfollowers = FollowersandFollowing.objects.filter(username=user.id,created=date.today()).exclude(followers="").count()
    
    followersdata = FollowersandFollowing.objects.filter(username=user.id).exclude(followers="")
    followingdata = FollowersandFollowing.objects.filter(username=user.id).exclude(following="")
    userdatas=[]
    usernamedatas=[]
    for followdata in followersdata:
        userdatas.append(User.objects.get(username=str(followdata.followers)))
        usernamedatas.append(str(followdata.followers))
        # print(userdatas)
        
    for followdata in followingdata:
        if followdata.following not in usernamedatas:
            userdatas.append(User.objects.get(username=str(followdata.following)))

    context = {'followersdata':userdatas,'todayfollowers':todayfollowers}
    return render(request,'user/messages.html',context)

@login_required(login_url='/login')
def userprofile(request):
    todayfollowers = FollowersandFollowing.objects.filter(username=request.user.id,created=date.today()).exclude(followers="").count()
    context={'todayfollowers':todayfollowers}
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

    return render(request,'user/userprofile.html',context)

def room(request,room_name):
    return render(request, 'user/chat/chatroom.html', {
        'room_name': room_name
    })
@login_required(login_url='/login')
def changepassword(request):
    isNullProfile(request)
    # fm = PasswordChangeForm(user=request.user)
    context={}
    todayfollowers = FollowersandFollowing.objects.filter(username=request.user.id,created=date.today()).exclude(followers="").count()
    context={'todayfollowers':todayfollowers}
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
    if not isNullProfile(request):
        return redirect("/userprofile")
    return render(request,'user/notifications.html')

@login_required(login_url='/login')
def profile(request):
    if not isNullProfile(request):
        return redirect("/userprofile")
    return render(request,'user/otheruserprofile.html')

@login_required(login_url='/login')
def followers(request):
    todayfollowers = FollowersandFollowing.objects.filter(username=request.user.id,created=date.today()).exclude(followers="").count()

    if not isNullProfile(request):
        return redirect("/userprofile")
    if request.method == "POST":
        isFollowing = request.POST.get('isFollowing')
        id = request.POST.get('id')
    user = User.objects.get(id=request.user.id)
    followersdata = FollowersandFollowing.objects.filter(username=user.id).exclude(followers="")
    userdatas=[]
    for followdata in followersdata:
        userdatas.append(User.objects.get(username=str(followdata.followers)))
        # print(userdatas)
        
    context = {'followersdata':userdatas,'todayfollowers':todayfollowers}
    # print(followersdata)
    return render(request,'user/followers.html',context)


@login_required(login_url='/login')
def searchuser(request):
    context={}
    todayfollowers = FollowersandFollowing.objects.filter(username=request.user.id,created=date.today()).exclude(followers="").count()
    context = {'todayfollowers':todayfollowers}
    
    if not isNullProfile(request):
        return redirect("/userprofile")
    if request.method == "POST":
        username = request.POST.get('username')
        isFollowing = request.POST.get('isFollowing')
        addfollowers = request.POST.get('addfollowers')

        if addfollowers == "True":
            followingdata = FollowersandFollowing.objects.create(username=request.user,following=username)
            followingdata.save()
            userdata = User.objects.get(username=username)
            followersdata = FollowersandFollowing.objects.create(username=userdata,followers=str(request.user))
            followersdata.save()
        elif addfollowers == "False":
            followersdata = FollowersandFollowing.objects.get(username=request.user,following=username)
            followersdata.delete()
            userdata = User.objects.get(username=username)
            followingdata = FollowersandFollowing.objects.get(username=userdata,followers=str(request.user))
            followingdata.delete()


        if User.objects.filter(username=username).exists() and not username == str(User.objects.get(id=request.user.id)):
            userdata = User.objects.get(username=username)
            if userdata.first_name=="":
                context["msg"]="User has not updated their profile...."
                return render(request,'user/searchuser.html',context)
            if userdata.profile.status==True:
                # isyourfollowers = FollowersData.objects.filter(user=request.user,username=username).count()
                # if isyourfollowers:
                #     data = FollowersData.objects.get(user=request.user,username=username)
                #     context["isfollowing"]=data.isFollowers
                # else:
                #     context["isfollowing"]=False
                #     context['Create']='Create'
                if FollowersandFollowing.objects.filter(username=request.user).exists():
                    userdata = User.objects.get(username=username)
                    # print(userdata)
                    youfollowing = FollowersandFollowing.objects.filter(username=userdata.id).exclude(following="").count()
                    yourfollowers = FollowersandFollowing.objects.filter(username=userdata.id).exclude(followers="").count()
                
                    context["following"]=youfollowing
                    context["followers"]=yourfollowers
                    if FollowersandFollowing.objects.filter(username=request.user,following=username).exists():
                        context["isfollowing"]=True
                    else:
                        context['isfollowing']=False
                else:
                    context["following"]=0
                    context["followers"]=0
                    context['isfollowing']=False

                context["image"]=userdata.profile.image.url
                context["firstname"]=userdata.first_name
                context["lastname"]=userdata.last_name
                context["bio"]=userdata.profile.aboutyourself
                context["Username"]=username

            return render(request,'user/searchuser.html',context)
        elif User.objects.filter(username=username).exists() and username == str(User.objects.get(id=request.user.id)):
            # context['msg']="same profile"
            return redirect("/userprofile")

        else:
            context["msg"]="User not found...."
            return render(request,'user/searchuser.html',context)
        # print(username)
    else:
        return redirect("/user")


@login_required(login_url='/login')
def following(request):
    todayfollowers = FollowersandFollowing.objects.filter(username=request.user.id,created=date.today()).exclude(followers="").count()

    if not isNullProfile(request):
        return redirect("/userprofile")
    if request.method == "POST":
        isFollowing = request.POST.get('isFollowing')
        id = request.POST.get('id')
    user = User.objects.get(id=request.user.id)
    followersdata = FollowersandFollowing.objects.filter(username=user.id).exclude(following="")
    userdatas=[]
    for followdata in followersdata:
        userdatas.append(User.objects.get(username=str(followdata.following)))
        
    context = {'followingdatas':userdatas,'todayfollowers':todayfollowers}
    return render(request,'user/following.html',context)
   
    

@login_required(login_url='/login') 
def updateTask(request):
    context={}
    if request.method == "POST":
        uid = request.POST.get('uid')
        editdata = request.POST.get('editdata')
        tasks = ToDoListData.objects.get(id=uid)
        tasks.title= editdata
        tasks.save()
        return redirect("/user")
        # print(uid,editdata)
    
    return redirect('/user')

@login_required(login_url='/login')
def deleteTask(request):
    if request.method == "POST":
        did = request.POST.get('did')
        tasks = ToDoListData.objects.get(id=did)
        tasks.delete()
        return redirect("/user")
        # print(uid,editdata)
    return redirect("/user")

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

   
    


