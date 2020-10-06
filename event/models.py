from django.db import models


sponsor_types = (
    ('altın','ALTIN'),
    ('gümüş','GÜMÜŞ'),
    ('bronz','BRONZ'),
    ('ürün','ÜRÜN'),
    ('destek','DESTEK'),
    ('medya','MEDYA'),
)


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    start_date = models.DateTimeField(auto_now_add=False,blank=True,null=True)
    end_date = models.DateTimeField(auto_now_add=False,blank=True,null=True)
    location = models.CharField(max_length=100,blank=True,null=True)
    poster = models.FileField(blank=True,null=True,verbose_name="Etkinlik Posteri")
    is_big_event = models.BooleanField(blank=True,null=True)

    def __str__(self):
        return self.title

class Sponsor(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="sponsor")
    name = models.CharField(max_length=20,verbose_name="Sponsorun adı")
    logo = models.FileField(blank=True,null=True,verbose_name="Sponsorun logosu")
    sponsorship_type = models.CharField(max_length=6,choices=sponsor_types)

    def __str__(self):
        return self.name + f" ({self.event.title})"

class Speaker(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="speaker")
    name = models.CharField(max_length=50,verbose_name="Konuşmacının adı")
    bio = models.TextField(verbose_name="Konuşmacı hakkında bilgi")
    photo = models.FileField(blank=True,null=True,verbose_name="Konuşmacının resmi")

    def __str__(self):
        return self.name + f" ({self.event.title})"
    