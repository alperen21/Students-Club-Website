from django.shortcuts import render
from .models import Event,Sponsor,Sponsor

# Create your views here.

def events(request):

    events = Event.objects.all()
    context = {
        "events":events,
    }

    return render(request,"events.html",context)