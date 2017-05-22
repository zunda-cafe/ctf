# -*- coding: utf-8 -*-

from django.conf.urls import url
from challenge import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/(?P<question_id>\d+)$', views.show, name='show'),
]
