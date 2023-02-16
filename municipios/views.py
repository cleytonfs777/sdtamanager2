from django.shortcuts import render
from djgeojson.views import GeoJSONLayerView


class MunicipiosGeojson(GeoJSONLayerView):
    ...