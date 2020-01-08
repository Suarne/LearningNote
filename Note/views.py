# Create your views here.

from django.shortcuts import render

from Note.models import Topic


def index(request):
    """ 学习笔记主页 """
    return render(request, 'index.html')


def topics(request):
    """ 主题主页 """
    topics = Topic.objects.order_by('date_added')
    context = { 'topics': topics }
    return render(request, 'topics.html', context)


def topic(request, topic_id):
    """ 记录 """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = { 'topic': topic, 'entries': entries }
    return render(request, 'topic.html', context)
