# Generated by Django 3.1.5 on 2022-11-06 18:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_videocontent_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocontent',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 6, 18, 31, 37, 569053, tzinfo=utc)),
        ),
    ]
