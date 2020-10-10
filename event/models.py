from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)

    content = models.TextField(verbose_name="Kısa tanıtım")
    details = models.TextField(verbose_name="Uzun tanıtım",blank=True,null=True)

    start_date = models.DateTimeField(auto_now_add=False,blank=True,null=True)
    end_date = models.DateTimeField(auto_now_add=False,blank=True,null=True)

    location = models.CharField(max_length=100,blank=True,null=True,verbose_name="Yer")
    location_url = models.CharField(max_length=100,blank=True,null=True,verbose_name="Google maps linki")
    iframe_url = models.CharField(max_length=1000,blank=True,null=True,verbose_name="iframe linki")

    poster = models.FileField(blank=True,null=True,verbose_name="Etkinlik Posteri")

    distinct_page = models.CharField(max_length=50, blank=True,null=True)
    distinct_ticket = models.CharField(max_length=50, blank=True,null=True)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['start_date']


class MainSponsor(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="MainSponsor")
    name = models.CharField(max_length=20,verbose_name="Sponsorun adı")
    logo = models.FileField(blank=True,null=True,verbose_name="Sponsorun logosu")
    url = models.CharField(max_length=1000,blank=True,null=True,verbose_name="Sponsor Sayfasının Linki")

    def __str__(self):
        return self.name + f" ({self.event.title})"

class GoldSponsor(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="GoldSponsor")
    name = models.CharField(max_length=20,verbose_name="Sponsorun adı")
    logo = models.FileField(blank=True,null=True,verbose_name="Sponsorun logosu")
    url = models.CharField(max_length=1000,blank=True,null=True,verbose_name="Sponsor Sayfasının Linki")

    def __str__(self):
        return self.name + f" ({self.event.title})"

class SilverSponsor(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="SilverSponsor")
    name = models.CharField(max_length=20,verbose_name="Sponsorun adı")
    logo = models.FileField(blank=True,null=True,verbose_name="Sponsorun logosu")
    url = models.CharField(max_length=1000,blank=True,null=True,verbose_name="Sponsor Sayfasının Linki")

    def __str__(self):
        return self.name + f" ({self.event.title})"

class BronzeSponsor(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="BronzeSponsor")
    name = models.CharField(max_length=20,verbose_name="Sponsorun adı")
    logo = models.FileField(blank=True,null=True,verbose_name="Sponsorun logosu")
    url = models.CharField(max_length=1000,blank=True,null=True,verbose_name="Sponsor Sayfasının Linki")

    def __str__(self):
        return self.name + f" ({self.event.title})"

class ItemSponsor(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="ItemSponsor")
    name = models.CharField(max_length=20,verbose_name="Sponsorun adı")
    logo = models.FileField(blank=True,null=True,verbose_name="Sponsorun logosu")
    url = models.CharField(max_length=1000,blank=True,null=True,verbose_name="Sponsor Sayfasının Linki")

    def __str__(self):
        return self.name + f" ({self.event.title})"

class MediaSponsor(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="MediaSponsor")
    name = models.CharField(max_length=20,verbose_name="Sponsorun adı")
    logo = models.FileField(blank=True,null=True,verbose_name="Sponsorun logosu")
    url = models.CharField(max_length=1000,blank=True,null=True,verbose_name="Sponsor Sayfasının Linki")

    def __str__(self):
        return self.name + f" ({self.event.title})"

class Speaker(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="Speaker")
    name = models.CharField(max_length=50,verbose_name="Konuşmacının adı")
    bio = models.TextField(verbose_name="Konuşmacı hakkında bilgi")
    photo = models.FileField(blank=True,null=True,verbose_name="Konuşmacının resmi")

    def __str__(self):
        return self.name + f" ({self.event.title})"
    