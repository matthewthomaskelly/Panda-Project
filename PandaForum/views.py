from django.shortcuts import render

from PandaForum.models import Topic, SubTopic, Thread, Reply

# Create your views here.

# Topic -> SubTopic -> Thread -> Reply

def index(request):

    context_dict = {}

    # get all topics
    Topics = Topic.objects.all()
    context_dict['topics'] = Topics
    print("Topics: " + str(Topics) )

    # loop through each topic and get related sub topics
    for eachTopic in Topics:
        context_dict[str(eachTopic)]['subtopics'] = {}
        SubTopics = eachTopic.subtopic_set.all()
        context_dict[str(eachTopic)]['subtopics'] = SubTopics
        print ("SubTopics: " + str(SubTopics) )
    
        # for each sub-topic, loop through each Thread
        for eachSubTopic in SubTopics:
            #context_dict[str(eachTopic)][str(eachSubTopic)] = {}
            context_dict[str(eachTopic)][str(eachSubTopic)]['threads'] = {}
            Threads = eachSubTopic.thread_set.all()
            context_dict[str(eachTopic)][str(eachSubTopic)]['threads'] = Threads
            print("Threads: " + str(Threads) )
    
            # for each thread, loop through each reply
            for eachThread in Threads:
                context_dict[str(eachTopic)][str(eachSubTopic)][str(eachThread)]['replies'] = {}    
                Replies = eachThread.reply_set.all()
                print ("Replies: " + str(Replies) )

                #context_dict[str(eachTopic)][str(eachSubTopic)][str(eachThread)] = Replies
                context_dict[str(eachTopic)][str(eachSubTopic)][str(eachThread)]['replies'] = Replies
            

    # this is the view
    return render(request, 'index.html', {"context_dict": context_dict} )
