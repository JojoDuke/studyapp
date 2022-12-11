from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
rooms = [
    {'id': 1, 'name': 'Learn Python'},
    {'id': 2, 'name': 'Its Django'},
    {'id': 3, 'name': 'Go Flask'}
]

def home(request):
    return render(request, 'home.html', {'rooms': rooms})

def rooms(request):
    return HttpResponse("Welcome to rooms")
