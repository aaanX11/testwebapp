
from django.conf.urls import url, include
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^/list_supplies/$', views.list_supplies, name='list_supplies'),
    url(r'^/list_users$', views.list_users),
    url(r'^/list_suggestions$', views.list_suggestions),
    url(r'^/supply/(?P<pk>\d+)/$', views.supply),
    url(r'^/suggestion/(?P<pk>\d+)$', views.suggestion),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


