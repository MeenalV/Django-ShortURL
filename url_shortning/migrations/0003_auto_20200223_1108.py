# Generated by Django 3.0.3 on 2020-02-23 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortning', '0002_auto_20200223_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urldata',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 23, 11, 8, 21, 803179)),
        ),
        migrations.AlterField(
            model_name='urldata',
            name='dateExpired',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 23, 11, 23, 21, 803205)),
        ),
    ]
