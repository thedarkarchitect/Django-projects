from django.shortcuts import render
from .models import Room, Message

from django.contrib.auth.decorators import login_required

# Create your views here.
#we must make sure the person that accesses the rooms is authenticated
@login_required
def rooms(request):
    rooms = Room.objects.all()
    context = {
        'rooms':rooms
    }
    return render(request, 'room/roomspage.html', context)

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    context = {
        'room':room,
        'messages':messages
    }
    return render(request, 'room/room.html', context)