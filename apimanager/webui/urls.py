# -*- coding: utf-8 -*-
"""
URLs for config app
"""

from django.conf.urls import url

from .views import IndexView
from .views import MethodRoutingView

urlpatterns = [
    url(r'^$',
        IndexView.as_view(),
        name='webui-index'),
]
