# Generated by Django 4.2.1 on 2023-06-01 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_useractivity_login_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
