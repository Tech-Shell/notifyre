# Generated by Django 3.0.7 on 2020-06-27 10:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20200627_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 27, 10, 11, 48, 448664, tzinfo=utc)),
        ),
    ]