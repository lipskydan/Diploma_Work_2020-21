# Generated by Django 3.0 on 2021-05-01 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_items', '0018_workreport_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workreport',
            name='created_date',
            field=models.DateTimeField(blank=True, verbose_name='Час створення'),
        ),
        migrations.AlterField(
            model_name='workreport',
            name='work_report_field',
            field=models.TextField(default='Опис проведених робіт', verbose_name='Опис проведених робіт'),
        ),
    ]
