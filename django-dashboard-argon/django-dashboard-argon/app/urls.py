# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from django.conf.urls import url

urlpatterns = [

    # The home page
    path('', views.form, name='home'),
    path('index/', views.index, name='index'),
    url(r'^extract', views.extract, name="extract"),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
