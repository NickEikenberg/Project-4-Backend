# Generated by Django 3.2.9 on 2021-11-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.CharField(default='', max_length=24),
        ),
    ]