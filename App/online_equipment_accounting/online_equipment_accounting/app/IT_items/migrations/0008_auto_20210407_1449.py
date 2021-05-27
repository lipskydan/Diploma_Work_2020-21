# Generated by Django 3.0 on 2021-04-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_items', '0007_solidstatedrive'),
    ]

    operations = [
        migrations.CreateModel(
            name='HardDiskDrive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='відсутній', max_length=200, verbose_name='бренд')),
                ('model', models.CharField(default='відсутній', max_length=200, verbose_name='модель')),
                ('serial_number', models.CharField(default='відсутній', max_length=200, unique=True, verbose_name='серійний номер')),
                ('memory_size', models.IntegerField(default=0, verbose_name="обсяг пам'яті")),
            ],
            options={
                'verbose_name': 'Жорсткий магнітний диск',
                'verbose_name_plural': 'Жорсткі магнітні диски',
            },
        ),
        migrations.AlterField(
            model_name='solidstatedrive',
            name='brand',
            field=models.CharField(default='відсутній', max_length=200, verbose_name='бренд'),
        ),
        migrations.AlterField(
            model_name='solidstatedrive',
            name='model',
            field=models.CharField(default='відсутній', max_length=200, verbose_name='модель'),
        ),
    ]