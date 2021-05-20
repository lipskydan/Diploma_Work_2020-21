# Generated by Django 3.0 on 2021-03-15 09:55

from django.db import migrations, models
import django.db.models.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('IT_items', '0004_auto_20210315_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='pc',
            name='optical_drive',
            field=models.ForeignKey(null=True, on_delete=django.db.models.fields.related.OneToOneField, to='IT_items.OpticalDrive'),
        ),
        migrations.AlterField(
            model_name='pc',
            name='place',
            field=models.IntegerField(blank=True, default=0, verbose_name='номер учбового місця'),
        ),
    ]
