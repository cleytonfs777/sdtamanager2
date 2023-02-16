from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Municipio


@admin.register(Municipio)
# class MunicipioAdmin(admin.ModelAdmin):
class MunicipioAdmin(LeafletGeoAdmin):
    list_display = ['name', 'cob']