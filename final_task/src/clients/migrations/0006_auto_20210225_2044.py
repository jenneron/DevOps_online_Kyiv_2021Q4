# Generated by Django 3.1.5 on 2021-02-25 20:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0005_auto_20210202_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unloading',
            name='workers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]