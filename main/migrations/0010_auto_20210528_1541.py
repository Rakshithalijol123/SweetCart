# Generated by Django 3.2.3 on 2021-05-28 15:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210527_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AlterField(
            model_name='review',
            name='posted_on',
            field=models.DateField(default=datetime.datetime(2021, 5, 28, 15, 41, 39, 795864, tzinfo=utc)),
        ),
    ]
