from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.index, name='index'),
    url(r'^Actualizar/(?P<recId>[0-9]+)$', views.actRecibo, name='actRecibo'),
    url(r'^actualizando/(?P<recId>[0-9]+)$', views.actualizar, name='actualizar'),
    url(r'^crear/$', views.crearRecibo, name='crearRecibo'),
    url(r'^eliminar/(?P<recId>[0-9]+)$', views.eliminarRecibo, name='eliminar'),

]
