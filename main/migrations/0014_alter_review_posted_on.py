# Generated by Django 3.2.3 on 2021-05-28 15:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_review_posted_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='posted_on',
            field=models.DateField(default=datetime.datetime(2021, 5, 28, 15, 55, 2, 366624, tzinfo=utc)),
        ),
    ]
