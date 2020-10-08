from django.shortcuts import render, get_object_or_404
from .models import Event,Sponsor,Sponsor

# Create your views here.

def events(request):

    events = Event.objects.all()
    context = {
        "events":events,
    }

    return render(request,"events.html",context)

def event(request,id):
    event = get_object_or_404(Event,id=id)
    
    context = {
        "event":event,
    }

    return render(request,"event.html",context)