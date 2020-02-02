from django.conf.urls import url
from .views import LoginView
from .views import LogoutView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView


urlpatterns = [
               url(r'^login/$', LoginView.as_view(), name='view_login'),
               url(r'^logout/$', LogoutView.as_view(), name='view_logout'),
               url(r'^reset/password/reset/$', PasswordResetView.as_view(template_name='usercustom/password_reset_form.html', email_template_name='usercustom/password_reset_email.html'), name='password_reset'),
		       url(r'^reset/password/reset/done/$', PasswordResetDoneView.as_view(template_name='usercustom/password_reset_done.html'), name='password_reset_done'),
		       url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(template_name='usercustom/password_reset_confirm.html'), name='password_reset_confirm'),
	    	   url(r'^reset/done/$', PasswordResetCompleteView.as_view(template_name='usercustom/password_reset_complete.html'), name='password_reset_complete'),
               url(r'^change/password/(?P<pk>[0-9]+)/$', PasswordChangeView.as_view(template_name='usercustom/password_change.html', success_url='/'), name='change_password'),
               ]