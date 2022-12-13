from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
rooms = [
    {'id': 1, 'name': 'Learn Python'},
    {'id': 2, 'name': 'Its Django'},
    {'id': 3, 'name': 'Go Flask'}
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def rooms(request, pk):
    return render(request,"base/rooms.html")
