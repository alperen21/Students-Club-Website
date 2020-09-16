from django.contrib import admin
from article.models import Article
from event.models import Event

# Register your models here.

admin.site.register(Article)
admin.site.register(Event)

