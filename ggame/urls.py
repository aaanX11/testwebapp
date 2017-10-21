
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.riddleshow, name='riddleshow'),
    url(r'^/game/$', views.game, name='game'),
]
