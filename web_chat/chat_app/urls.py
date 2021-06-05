from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'web_chat-home'),
    path('about/', views.about, name = 'web_chat-about'),
    path('chat/<str:room_name>/', views.room, name='web_chat-room'),
]