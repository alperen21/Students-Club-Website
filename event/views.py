from django.shortcuts import render, get_object_or_404
from .models import Event,MediaSponsor,MainSponsor, GoldSponsor,SilverSponsor,BronzeSponsor,MediaSponsor,ItemSponsor,Speaker

# Create your views here.

def events(request):

    events = Event.objects.all()
    context = {
        "events":events,
    }

    return render(request,"events.html",context)

def event(request,id):
    event = get_object_or_404(Event,id=id)
    mainsponsors = event.MainSponsor.all()
    goldsponsors = event.GoldSponsor.all()
    silversponsors = event.SilverSponsor.all()
    bronzesponsors = event.BronzeSponsor.all()
    itemsponsors = event.ItemSponsor.all()
    mediasponsors = event.MediaSponsor.all()
    
    context = {
        "event":event,
        "mainsponsors":mainsponsors,
        "goldsponsors":goldsponsors,
        "silversponsors":silversponsors,
        "bronzesponsors":bronzesponsors,
        "itemsponsors":itemsponsors,
        "mediasponsors":mediasponsors,
    }

    return render(request,"event.html",context)

def event_sponsors(request,id):
    event = get_object_or_404(Event,id=id)
    mainsponsors = event.MainSponsor.all()
    goldsponsors = event.GoldSponsor.all()
    silversponsors = event.SilverSponsor.all()
    bronzesponsors = event.BronzeSponsor.all()
    itemsponsors = event.ItemSponsor.all()
    mediasponsors = event.MediaSponsor.all()

    context = {
        "event":event,
        "mainsponsors":mainsponsors,
        "goldsponsors":goldsponsors,
        "silversponsors":silversponsors,
        "bronzesponsors":bronzesponsors,
        "itemsponsors":itemsponsors,
        "mediasponsors":mediasponsors,
    }
    return render(request,"event_sponsors.html",context)

def event_speakers(request,id):
    event = get_object_or_404(Event,id=id)
    speakers = event.Speaker.all()
    mainsponsors = event.MainSponsor.all()
    goldsponsors = event.GoldSponsor.all()
    silversponsors = event.SilverSponsor.all()
    bronzesponsors = event.BronzeSponsor.all()
    itemsponsors = event.ItemSponsor.all()
    mediasponsors = event.MediaSponsor.all()

    context = {
        "event":event,
        "speakers":speakers,
        "mainsponsors":mainsponsors,
        "goldsponsors":goldsponsors,
        "silversponsors":silversponsors,
        "bronzesponsors":bronzesponsors,
        "itemsponsors":itemsponsors,
        "mediasponsors":mediasponsors,
    }
    return render(request,"event_speakers.html",context)

def event_join(request,id):
    event = get_object_or_404(Event,id=id)
    mainsponsors = event.MainSponsor.all()
    goldsponsors = event.GoldSponsor.all()
    silversponsors = event.SilverSponsor.all()
    bronzesponsors = event.BronzeSponsor.all()
    itemsponsors = event.ItemSponsor.all()
    mediasponsors = event.MediaSponsor.all()

    context = {
        "event":event,
        "mainsponsors":mainsponsors,
        "goldsponsors":goldsponsors,
        "silversponsors":silversponsors,
        "bronzesponsors":bronzesponsors,
        "itemsponsors":itemsponsors,
        "mediasponsors":mediasponsors,
    }

    return render(request,"event_join.html",context)
