from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name="Makale Başlığı")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(blank=True,null=True,verbose_name="Makale Resmi")
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    check = models.BooleanField(default=False)

    def __str__(self):
        return self.title