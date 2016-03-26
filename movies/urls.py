from django.conf.urls import url

from . import views

urlpatterns = [
    #Url movies/
    url(r'^$', views.index, name='index'),
    #Url movies/2/
    url(r'(?P<movie_id>[0-9]+)/$', views.fiche, name='fiche'),
    #Url movies/wanted/
    url(r'^wanted/$', views.wanted, name='wanted'),
    #Url movies/manage/
    url(r'^manage/$', views.manage, name='manage'),
]