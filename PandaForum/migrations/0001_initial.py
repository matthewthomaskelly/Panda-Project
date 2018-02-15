# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-08 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_text', models.CharField(max_length=1024)),
            ],
            options={
                'verbose_name_plural': 'Replies',
            },
        ),
        migrations.CreateModel(
            name='SubTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_text', models.CharField(max_length=1024)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PandaForum.SubTopic')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='subtopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PandaForum.Topic'),
        ),
        migrations.AddField(
            model_name='reply',
            name='reply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PandaForum.Thread'),
        ),
    ]