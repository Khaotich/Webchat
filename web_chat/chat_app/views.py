from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'chat_app/home.html', {'title':'Home Page'})

def about(request):
    return render(request, 'chat_app/about.html', {'title':'About'})

@login_required
def room(request, room_name):
    return render(request, 'chat_app/room.html', {
        'room_name': room_name,
        'title': room_name
    })