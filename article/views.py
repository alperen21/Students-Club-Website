from django.shortcuts import render, redirect
from contact.forms import contact_form
from django.contrib import messages
from contact.webmail import send_mail
from article.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

# Create your views here.

def Index(request):
    return render(request,"index.html")

def test(request):
    return render(request,"text.html")

def login_user(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form,
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Kullanıcı adı veya parola yanlış")
            return render(request,"login.html",context)
        else:
            login(request,user)
            messages.success(request,"Başarıyla giriş yaptın",context)

            

    return render(request,"login.html",context)

def logout_user(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptın")
    return redirect("article:login")