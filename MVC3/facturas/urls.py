from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
    url(r'^facturas/$', CreateView.as_view(), name="create"),
    
    url(r'^facturas/(?P<pk>[0-9]+)/$',DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)