# Generated by Django 3.0 on 2021-04-16 07:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IT_items', '0017_workreport_work_report_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='workreport',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]