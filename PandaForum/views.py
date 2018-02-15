from django.shortcuts import render

from PandaForum.models import Topic, SubTopic, Thread, Reply

# Create your views here.

# Topic -> SubTopic -> Thread -> Reply

def index(request):

    context_dict = {}

    topics = Topic.objects.all()
    context_dict['topics'] = topics

    context_dict['subtopics'] = {}
    for each in topics:
        print(each)
        subtopics = SubTopic.objects.filter(topic=each)
        context_dict['subtopics'].update( subtopics )

    context_dict['threads'] = {}
    for each in subtopics:
        print (each)
        threads = Thread.objects.filter(thread=each)
        context_dict['threads'].update(threads)

    context_dict['replies'] = {}
    for each in threads:
        print(each)
        replies = Reply.objects.filter(reply=each)
        context_dict['replies'].update(replies)

    # this is the view
    return render(request, 'index.html', context_dict)

