# Generated by Django 3.0.8 on 2020-07-20 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_auto_20200711_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
