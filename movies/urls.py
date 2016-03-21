from django.conf.urls import url

from . import views

urlpatterns = [
    #Url /
    url(r'^$', views.index, name='index'),
    #Url /wanted/
    url(r'^wanted/$', views.wanted, name='wanted'),
    #Url /manage/
    url(r'^manage/$', views.manage, name='manage'),
]