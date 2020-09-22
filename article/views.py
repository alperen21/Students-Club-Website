from django.shortcuts import render
from contact.forms import contact_form
from django.contrib import messages
from contact.webmail import send_mail

# Create your views here.

def Index(request):
    return render(request,"index.html")

def test(request):
    return render(request,"test.html")