# Generated by Django 3.2.3 on 2021-05-26 08:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210522_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='posted_on',
            field=models.DateField(default=datetime.datetime(2021, 5, 26, 8, 21, 46, 838108, tzinfo=utc)),
        ),
    ]
