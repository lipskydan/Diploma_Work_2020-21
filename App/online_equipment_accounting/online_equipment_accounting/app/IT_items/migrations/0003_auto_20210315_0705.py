# Generated by Django 3.0 on 2021-03-15 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_items', '0002_auto_20210314_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opticaldrive',
            name='type_connector',
            field=models.CharField(choices=[('не вказано', ''), ('SATA', 'SATA'), ('PATA', 'PATA')], default='не вказано', max_length=20),
        ),
    ]
