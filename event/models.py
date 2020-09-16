from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)