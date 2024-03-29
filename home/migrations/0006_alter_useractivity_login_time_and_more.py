# Generated by Django 4.2.1 on 2023-06-01 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_alter_useractivity_login_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='login_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='useractivity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
