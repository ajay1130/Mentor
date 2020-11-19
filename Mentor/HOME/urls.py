from django.contrib import admin
from django.urls import path,re_path,include
from HOME import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'HOME'
urlpatterns = [
    path('', views.index,name="Home"),
    path('index', views.index,name="Home"),
    path('about',views.about,name="About"),
    path('contact', views.contact,name="Contact"),
    path('login',views.loginUser,name="Login"),
    path('register',views.register,name="Register"),
    path('user',views.user,name="User"),
    path('messages',views.messagesuser,name="Messages"),
    path('userprofile',views.userprofile,name="Userprofile"),
    path('changepassword',views.changepassword,name="Changepassword"),
    # path('notifications',views.notifications,name="Notifications"),
    path('logout', views.logoutUser, name='Logout'),
    path('userchat/',views.chat,name="Chat"),
    path('userchat/<str:room_name>/',views.room,name="ChatRoom"),
    path('profile',views.profile,name="profile"),
    path('followers',views.followers,name="followers"),
    path('following',views.following,name="following"),
    path('searchuser',views.searchuser,name="searchuser"),
    path('updatetask',views.updateTask,name="updatetask"),
    path('deletetask',views.deleteTask,name="deletetask"),
    path('forgetpassword',views.forgetpassword,name="forgetpassword"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    # path('account/', include('django.contrib.auth.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)