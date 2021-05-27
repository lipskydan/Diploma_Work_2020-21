# Generated by Django 3.0 on 2021-04-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_items', '0013_auto_20210409_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='motherboard',
            name='central_processing_unit',
            field=models.CharField(choices=[('не вказано', ''), ('Intel Core i7', 'Intel Core i7'), ('Intel Core i5', 'Intel Core i5'), ('Intel Core i3', 'Intel Core i3'), ('Intel Core Pentium', 'Intel Core Pentium'), ('Intel Core 2 Duo', 'Intel Core 2 Duo')], default='не вказано', max_length=20),
        ),
    ]