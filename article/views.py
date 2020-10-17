from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import contact_form
from article.forms import ArticleForm
from django.contrib import messages
from contact.webmail import send_mail
from article.forms import LoginForm
from django.contrib.auth.models import User
from .models import Article
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from event.models import Event
from contact.forms import mail_list_form
# Create your views here.

def Index(request):
    events = Event.objects.all()
    form = mail_list_form(request.POST or None)
    articles = Article.objects.all()[:3]
    if request.method == "POST":
        email = request.POST.get("email")

    context = {
        "events":events,
        "form":form,
        "articles":articles,
    }
    return render(request,"index.html",context)

def test(request):
    return render(request,"text.html")

def login_user(request):
    events = Event.objects.all()
    form = LoginForm(request.POST or None)

    context = {
        "form":form,
        "events":events,
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
            messages.success(request,"Başarıyla giriş yaptın")

    return render(request,"login.html",context)

@login_required
def logout_user(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptın")
    return redirect("article:login")

@login_required(login_url="article:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    form = ArticleForm(request.POST or None, request.FILES or None)
    events = Event.objects.all()
    context = {
        "form":form,
        "articles":articles,
        "events":events,
    }
    try:
        
        if form.is_valid():

            new_article = form.save(commit=False)
            new_article.author = request.user
            new_article.save()

            messages.success(request,"Makale eklendi")

    except:

        messages.info(request,"Bir problem oluştu")


    return render(request,"new_article.html",context)

@login_required(login_url="article:login")
def panel(request):
    events = Event.objects.all()
    context = {
        "events":event
    }
    return render(request,"panel.html",context)

def blog(request):
    articles = Article.objects.all()
    events = Event.objects.all()
    context = {
        "articles":articles,
        "events":events,
    }
    return render(request,"blog.html",context)

def article(request,id):
    article = get_object_or_404(Article,id=id)
    events = Event.objects.all()
    context = {
        "article":article,
        "events":events,
    }
    return render(request,"article.html",context)

