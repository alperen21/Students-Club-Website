from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Event)
admin.site.register(models.Speaker)
admin.site.register(models.MainSponsor)
admin.site.register(models.GoldSponsor)
admin.site.register(models.SilverSponsor)
admin.site.register(models.BronzeSponsor)
admin.site.register(models.MediaSponsor)
admin.site.register(models.ItemSponsor)
