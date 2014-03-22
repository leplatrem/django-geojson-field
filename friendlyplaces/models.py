from django.db import models

from djgeojson.fields import GeoJSONField


class FriendlyPlace(models.Model):

    name = models.CharField(max_length=200)
    wifi = models.BooleanField()
    power = models.BooleanField()

    geom = GeoJSONField()

    def __unicode__(self):
        return self.name
