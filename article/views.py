from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request,"index.html")

def test(request):
    return render(request,"test.html")