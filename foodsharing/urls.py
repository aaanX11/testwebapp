
from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
#

urlpatterns = [
    url(r'^home/$', 				views.home),
    url(r'^$', 						views.list_supplies, name='list_supplies'),
    url(r'^list_users/$', 			views.list_users,name='list_users'),
    url(r'^list_suggestions/$', 	views.list_suggestions, name='list_suggestions'),
    url(r'^supply/(?P<pk>\d+)/$', 	views.supply, name='supply'),
    url(r'^user/(?P<pk>\d+)/$', 	views.user, name='user'),
    url(r'^suggestion/(?P<pk>\d+)/$', views.suggestion, name='suggestion'),
    url(r'^login/$', 				auth_views.login, name='login'),
    url(r'^logout/$', 				auth_views.logout,{'next_page': '/'}, name='logout'),
    url(r'^signup/$', 				views.signup, name='signup'),
    url(r'^supp_form/$', 			views.supp_form, name='supp_form'),
    url(r'^sugg_form/$', 			views.sugg_form, name='sugg_form'),
    url(r'^test_ajax/$', 			views.home, name='test_ajax'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


