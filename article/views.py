from django.shortcuts import render
from contact.forms import contact_form
from django.contrib import messages
from contact.webmail import send_mail

# Create your views here.

def Index(request):
    return render(request,"index.html")

def test(request):
    return render(request,"test.html")

def contact(request):
    form = contact_form(request.POST or None)
    if request.method == "POST":

        email = request.POST.get("email")
        name = request.POST.get("name")
        body = request.POST.get("message")

        if send_mail(email,body,name):
            messages.success(request,"Mesajınız başarıyla alındı")
        else:
            messages.info(request,"Bir sorun çıktı")

    context = {
        "contact_form":form,
    }
    return render(request,"contact.html",context)