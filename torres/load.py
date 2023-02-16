import os

from django.contrib.gis.utils import LayerMapping

from .models import Torre

torre_mapping = {
    'name': 'name',
    'description': 'description',
    'abrigo': 'ABRIGO',
    'aceitacao': 'ACEITACAO',
    'ad_infra': 'AD_INFRA',
    'ar_condicionado': 'AR_CONDICIONADO',
    'aut_pmmg': 'AUT_PMMG',
    'bbm': 'BBM',
    'cob': 'COB',
    'convenio': 'CONVENIO',
    'energia_cedida': 'ENERGIA_CEDIDA',
    'fracao': 'FRACAO',
    'instalado': 'INSTALADO',
    'inst_conf_enl': 'INST_CONF_ENL',
    'inst_conf_rep': 'INST_CONF_REP',
    'inst_gab': 'INST_GAB',
    'inst_sis_irr': 'INST_SIS_IRR',
    'latitude': 'LATITUDE',
    'laudo': 'LAUDO',
    'lic_anatel': 'LIC_ANATEL',
    'longitude': 'LONGITUDE',
    'nec_abrigo': 'NEC_ABRIGO',
    'obs': 'OBS',
    'padrão': 'PADRÃO',
    'propriedade': 'PROPRIEDADE',
    'prospeccao': 'PROSPECCAO',
    'pte': 'PTE',
    'resp_nome': 'RESP_NOME',
    'resp_tel': 'RESP_TEL',
    'seguranca': 'SEGURANCA',
    'geom': 'POINT25D',
}


shp = os.path.abspath(os.path.join('data', 'torres.geojson'))

def run_torre(verbose=True):
    lm = LayerMapping(Torre, shp, torre_mapping)
    lm.save(strict=True, verbose=True)