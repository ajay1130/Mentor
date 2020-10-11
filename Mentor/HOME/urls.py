from django.contrib import admin
from django.urls import path
from HOME import views

urlpatterns = [
    path('', views.index,name="Home"),
    path('index', views.index,name="Home"),
    path('about',views.about,name="About"),
    path('contact', views.contact,name="Contact"),
    path('login',views.login,name="Login"),
    path('register',views.register,name="Register"),
    path('user',views.user,name="User"),
    path('messages',views.messages,name="Messages"),
    path('chat',views.chat,name="Chat"),
    path('demochat',views.demoChat,name="Demochat"),
    path('userprofile',views.userprofile,name="Userprofile"),
    path('changepassword',views.changepassword,name="Changepassword"),
    path('notifications',views.notifications,name="Notifications")
]