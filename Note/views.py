# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import EntryForm, TopicForm
from .models import Entry, Topic


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


def new_topic(request):
    """ 添加新主题 """
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('LearningNote:topics'))

    context = { 'form': form }
    return render(request, 'new_topic.html', context)


def new_entry(request, topic_id):
    """ 在特定的主题中添加新的记录 """
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('LearningNote:topic', args=[ topic_id ]))

    context = { 'topic': topic, 'form': form }
    return render(request, 'new_entry.html', context)


def edit_entry(request, entry_id):
    """ 编辑已有的学习笔记 """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('LearningNote:topic', args=[ topic.id ]))

    context = { 'entry': entry, 'topic': topic, 'form': form }
    return render(request, 'edit_entry.html', context)
