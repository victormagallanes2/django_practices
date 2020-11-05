from django.conf.urls import url
from .views import UserListAPI
from .views import UserDetailAPI
from .views import UserCreateAPI
from .views import UserUpdateAPI
from .views import UserDeleteAPI


urlpatterns = [
               url(r'^users/list/$', UserListAPI.as_view()),
               url(r'^users/create/$', UserCreateAPI.as_view()),
               url(r'^users/detail/(?P<pk>[0-9]+)/$', UserDetailAPI.as_view()),
               url(r'^users/update/(?P<pk>[0-9]+)/$', UserUpdateAPI.as_view()),
               url(r'^users/delete/(?P<pk>[0-9]+)/$', UserDeleteAPI.as_view()),

              ]
