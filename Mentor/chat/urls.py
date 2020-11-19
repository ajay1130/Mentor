from django.contrib import admin
from django.urls import path,re_path,include
from chat import views
urlpatterns = [
    path('', views.index,name="index"),
    path('<str:room_name>/', views.room,name="room"),
    path('getusername',views.getusername,name="getusername"),
    path('tempchatroom',views.tempchatroom,name="tempchatroom"),
    path('fetchremdata',views.fetchdremdata,name="fetchremdata"),
]
