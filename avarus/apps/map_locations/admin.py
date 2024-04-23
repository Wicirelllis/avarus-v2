from django.contrib import admin

from .models import MapLocation


class MapLocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(MapLocation, MapLocationAdmin)
