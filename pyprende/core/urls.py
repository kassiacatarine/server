from django.conf.urls import url
from pyprende.core import views # Importa as funções existentes na view do app core


urlpatterns = [
    url(r'^$', views.home, name='home'),# Chama a função existente na view
    url(r'^contato/', views.contact, name='contact'),
]