from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.contrib import admin

from djgeojson.views import GeoJSONLayerView

from .models import FriendlyPlace


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=FriendlyPlace), name='data'),
    url(r'^admin/', include(admin.site.urls)),
)
