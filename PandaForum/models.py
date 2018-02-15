from django.db import models

# Create your models here.
class Topic(models.Model):

    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class SubTopic(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=128)

    def __str__(self):
        return self.sub_title

class Thread(models.Model):

    thread = models.ForeignKey(SubTopic, on_delete=models.CASCADE)
    thread_text = models.CharField(max_length=1024)
    

class Reply(models.Model):

    reply = models.ForeignKey(Thread, on_delete=models.CASCADE)
    reply_text = models.CharField(max_length=1024)

    class Meta:
        verbose_name_plural = 'Replies'
