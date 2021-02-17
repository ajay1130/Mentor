from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json
from django.contrib.auth import get_user_model
from .models import *
from django.http import JsonResponse

User = get_user_model()
username=""
# Create your views here.
def index(request):
    # return render(request,'user/messages.html',{})
    return redirect("/messages")

def getusername(request):
    # return render(request,'user/messages.html',{})
    if request.method == "POST":
        global username
        username = request.POST.get('username')
        # if not ('username' in request.session):
        #      
        request.session['username']=username
        print(username)
        content = request.POST.get('content')
        if content == "123_FILE_UPLOAD":
            filedata = request.FILES["fileupload"]
            Message.objects.create(author=request.user,content=content,rauthor=str(request.session.get('username')),filedata=filedata)
    return redirect("/chat/chatroom/")

def tempchatroom(request):
    return render(request,'user/tempchatpage.html',{})
# def getUserName():
#     print(type(username))

def fetchdremdata(request):
    messagesdata = Message.last_10_messages(author=request.user,rauthor=request.session['username'])
    # print(messagesdata.values())
    return JsonResponse({"fulldatas":list(messagesdata.values())})


@login_required(login_url='/login')
def room(request,room_name):
    if 'username' in request.session and room_name =="chatroom":
        userdata = User.objects.get(username=request.session['username'])
        sameuser = User.objects.get(username=request.user.username)
        messagesdata = Message.last_10_messages(author=sameuser,rauthor=userdata)

        return render(request,'user/chattemplate.html',{'room_name':mark_safe(json.dumps(room_name)),
        'username':mark_safe(json.dumps(request.user.username)),
        'currentuser':sameuser.username,
        'displayusername':userdata.username,
        'sendurl':sameuser.profile.image.url,
        'receiveurl':userdata.profile.image.url,
        'messagedatas':messagesdata,
        'reciverusername':mark_safe(json.dumps(username))
        })
    else:
        return redirect("/messages")