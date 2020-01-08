""" 定义LearningNote的URL模式 """

from django.conf.urls import url

from . import views

urlpatterns = [
    # home page
    url('^$', views.index, name='index'),
    # show all topics
    url('^topics/$', views.topics, name='topics'),
    # show the topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
