from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.home),
    url(r'^search$',views.search),
    url(r'^form$',views.form),
    url(r'^test$',views.test),
    url(r'^details/(?P<pk>\d+)/$', views.details),
    url(r'^book/(?P<pk>\d+)/$',views.bookDoctor),
    url(r'^reg$', views.register),
    url(r'^book/(?P<pk>\d+)/booked$', views.booked, name = 'bookedurl'),
    url(r'^(?P<pk>\d+)/history', views.history, name='history'),
]