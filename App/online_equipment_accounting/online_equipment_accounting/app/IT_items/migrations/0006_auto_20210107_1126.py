# Generated by Django 3.0 on 2021-01-07 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_items', '0005_auto_20210107_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motherboard',
            name='form_factor',
            field=models.CharField(choices=[('не вказано', ''), ('ATX', 'ATX'), ('microATX', 'microATX'), ('Mini-ITX', 'Mini-ITX'), ('Nano-ITX', 'Nano-ITX'), ('Pico-ITX', 'Pico-ITX')], max_length=20),
        ),
    ]
