from django.contrib import admin

# Register your models here.
from PandaForum.models import Topic, SubTopic, Thread, Reply

admin.site.register(Topic)
admin.site.register(SubTopic)
admin.site.register(Thread)
admin.site.register(Reply)