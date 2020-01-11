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
    # add new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # add new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # edit entries
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
