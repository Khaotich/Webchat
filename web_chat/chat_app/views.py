from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'chat_app/home.html')


def about(request):
    return render(request, 'chat_app/about.html', {'title': 'About'})
