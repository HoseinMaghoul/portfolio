# Generated by Django 3.1.7 on 2021-04-03 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
