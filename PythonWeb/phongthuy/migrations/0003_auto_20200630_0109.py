# Generated by Django 2.2.6 on 2020-06-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phongthuy', '0002_auto_20200630_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='namsinh',
            name='namsinh',
            field=models.CharField(max_length=5, unique=True, verbose_name='Năm sinh'),
        ),
    ]