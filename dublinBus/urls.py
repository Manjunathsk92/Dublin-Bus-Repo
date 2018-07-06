from django.conf.urls import url
from . import views
from django.urls import path

app_name='dublinBus'

urlpatterns = [
	url(r'^home_page$', views.about, name='home_page'),
	url(r'^map.html',views.map_reader,name='mapreader'),
        url(r'^heatmap_html',views.heatmap,name='heatmap'),
        url(r'^get_routes/',views.get_routes,name='routes'),
    url(r'^signup/$', views.signup_view, name='signup'),
url(r'^$', views.login_view, name='login'),
url(r'^logout/$', views.logout_view, name='logout'),
url(r'^test$', views.test_view, name='test'),
]
