from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import FriendlyPlace


admin.site.register(FriendlyPlace, LeafletGeoAdmin)
