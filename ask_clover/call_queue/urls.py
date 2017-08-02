from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^queued_calls$', views.queued_calls, name='queued_calls'),
    url(r'^add_call$', views.add_call, name='add_call'),
    url(r'^thanks$', views.thanks, name='thanks'),
]
