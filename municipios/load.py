import os

from django.contrib.gis.utils import LayerMapping

from .models import Municipio

municipio_mapping = {
    'name': 'name',
    'cob': 'COB',
    'geom': 'MULTIPOLYGON',
}

shp = os.path.abspath(os.path.join('data', 'municipiocob.geojson'))

def run_municipio(verbose=True):
    lm = LayerMapping(Municipio, shp, municipio_mapping)
    lm.save(strict=True, verbose=True)