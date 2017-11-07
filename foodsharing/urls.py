
from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.list_supplies, name='list_supplies'),
    url(r'^/list_users/$', views.list_users),
    url(r'^/list_suggestions/$', views.list_suggestions, name='list_suggestions'),
    url(r'^supply/(?P<pk>\d+)/$', views.supply, name='supply'),
    url(r'^suggestion/(?P<pk>\d+)/$', views.suggestion, name='suggestion'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


