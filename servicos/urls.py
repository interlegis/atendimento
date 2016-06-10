from __future__ import absolute_import
from django.conf.urls import include, url

from servicos.views import SistemaCrud, SolicitacaoCrud

from .apps import AppConfig

app_name = AppConfig.name

urlpatterns = [
    url(ur'sistema/', include(SistemaCrud.get_urls())),
    url(ur'solicitacao/', include(SolicitacaoCrud.get_urls())),
]
