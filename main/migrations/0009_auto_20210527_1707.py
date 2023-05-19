# Generated by Django 3.2.3 on 2021-05-27 17:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_alter_review_posted_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='posted_on',
            field=models.DateField(default=datetime.datetime(2021, 5, 27, 17, 5, 37, 590837, tzinfo=utc)),
        ),
    ]