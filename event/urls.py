"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from event import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "event"

urlpatterns = [
    path('/',views.events,name="events"),
    path('/<int:id>',views.event,name="event"),
    path('/<int:id>/sponsors',views.event_sponsors,name="event_sponsors"),
    path('/<int:id>/speakers',views.event_speakers,name="event_speakers"),
    path('/<int:id>/join',views.event_join,name="event_join"),
] 

