from django.contrib.gis.db import models


class Torre(models.Model):
    name = models.CharField('nome', max_length=100)
    abrigo = models.CharField('abrigo', max_length=5)
    aceitacao = models.CharField('aceitaçao', max_length=5)
    ad_infra = models.CharField('infraestrutura', max_length=5)
    ar_condicionado = models.CharField('ar_condicionado', max_length=5)
    aut_pmmg = models.CharField('autorizacao_pmmg', max_length=5)
    bbm = models.CharField('batalhao', max_length=8)
    cob = models.CharField('cob', max_length=8)
    convenio = models.CharField('convenio', max_length=5)
    energia_cedida = models.CharField('energia', max_length=25)
    fracao = models.CharField('fracao', max_length=30)
    instalado = models.CharField('instalado', max_length=5)
    inst_conf_enl = models.CharField('instalacao_configuracao_enlace', max_length=5)
    inst_conf_rep = models.CharField('instalacao_configuracao_repetidora', max_length=5)
    inst_gab = models.CharField('instalacao_gabinete', max_length=5)
    inst_sis_irr = models.CharField('instal_sistema_radiante', max_length=5)
    latitude = models.CharField('latitude', max_length=15)
    laudo = models.CharField('laudo', max_length=5)
    lic_anatel = models.CharField('licenca_anatel', max_length=5)
    longitude = models.CharField('longitude', max_length=15)
    nec_abrigo = models.CharField('abrigo', max_length=5)
    obs = models.CharField('observacoes', max_length=900)
    padrão = models.CharField('padrao', max_length=6)
    propriedade = models.CharField('propriedade', max_length=150)
    prospeccao = models.CharField('prospeccao', max_length=8)
    pte = models.CharField('projeto_tecnico_executivo', max_length=50)
    resp_nome = models.CharField('responsavel_nome', max_length=170)
    resp_tel = models.CharField('responsavel_telefone', max_length=170)
    seguranca = models.CharField('seguranca', max_length=300)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return self.name
    
