from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name="Makale Başlığı")
    content = models.TextField(verbose_name="Makale İçeriği")
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(blank=True,null=True,verbose_name="Makale Resmi")
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)