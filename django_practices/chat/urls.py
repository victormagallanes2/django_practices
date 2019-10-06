# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^chat_list/$', view=views.UserListView.as_view(), name='user_list'
    ),
]