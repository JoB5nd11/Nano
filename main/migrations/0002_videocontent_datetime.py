# Generated by Django 3.1.5 on 2022-11-06 16:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocontent',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 6, 16, 42, 16, 620964, tzinfo=utc)),
        ),
    ]