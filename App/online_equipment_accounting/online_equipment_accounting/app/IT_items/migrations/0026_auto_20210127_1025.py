# Generated by Django 3.0 on 2021-01-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_items', '0025_auto_20210127_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motherboard',
            name='serial_number',
            field=models.CharField(default='відсутній', max_length=200, unique=True, verbose_name='серійний номер'),
        ),
    ]
