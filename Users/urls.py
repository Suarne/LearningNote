""" 定义Users的URL模式 """

from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # login
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    # sign out
    url(r'^logout/$', views.logout_view, name='logout'),
    # register
    url(r'^regidter/$', views.register, name='register'),
]
app_name = 'Users'
