from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_Length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("auth.user", on_delete=False)