# Generated by Django 3.0 on 2021-04-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_items', '0009_auto_20210408_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc',
            name='place',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='номер учбового місця'),
        ),
        migrations.AlterField(
            model_name='pc',
            name='text_field',
            field=models.TextField(default='Місце для нотаток', null=True),
        ),
    ]
