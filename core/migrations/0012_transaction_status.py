# Generated by Django 3.1.3 on 2021-09-21 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_courier_paypal_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('in', 'IN'), ('out', 'OUT')], default='in', max_length=20),
        ),
    ]
