# -*- coding: utf-8 -*-

from django.conf.urls import url
from challenge import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/(?P<question_id>\d+)$', views.show, name='question.show'),
    url(r'^question/(?P<question_id>\d+)/good$', views.good, name='question.good'),
    url(r'^question/(?P<question_id>\d+)/mistake$', views.mistake, name='question.mistake'),
]
