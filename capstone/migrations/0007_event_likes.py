# Generated by Django 2.1.5 on 2022-06-17 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0006_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
