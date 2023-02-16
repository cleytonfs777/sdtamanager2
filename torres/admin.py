from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Torre


@admin.register(Torre)
class TorreAdmin(LeafletGeoAdmin):
    list_display = ['name', 'abrigo', 'aceitacao', 'ad_infra', 'ar_condicionado', 'aut_pmmg', 'bbm', 'cob', 'convenio', 'energia_cedida', 'fracao', 'instalado', 'inst_conf_enl', 'inst_conf_rep', 'inst_gab', 'inst_sis_irr', 'latitude', 'laudo', 'lic_anatel', 'longitude', 'nec_abrigo', 'obs', 'padrão', 'propriedade', 'prospeccao', 'pte', 'resp_nome', 'resp_tel', 'seguranca']