# Generated by Django 3.1.3 on 2021-09-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210916_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='distance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]