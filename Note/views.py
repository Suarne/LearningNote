# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import EntryForm, TopicForm
from .models import Entry, Topic


def index(request):
    """ 学习笔记主页 """
    return render(request, 'index.html')


@login_required
def topics(request):
    """ 主题主页 """
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = { 'topics': topics }
    return render(request, 'topics.html', context)


@login_required
def topic(request, topic_id):
    """ 记录 """
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = { 'topic': topic, 'entries': entries }
    return render(request, 'topic.html', context)


@login_required
def new_topic(request):
    """ 添加新主题 """
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('LearningNote:topics'))

    context = { 'form': form }
    return render(request, 'new_topic.html', context)


@login_required
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


@login_required
def edit_entry(request, entry_id):
    """ 编辑已有的学习笔记 """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('LearningNote:topic', args=[ topic.id ]))

    context = { 'entry': entry, 'topic': topic, 'form': form }
    return render(request, 'edit_entry.html', context)
