# Generated by Django 2.2.6 on 2020-05-29 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanpham', '0003_auto_20200529_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanpham',
            name='DaBan',
            field=models.BooleanField(default=False, verbose_name='Đã bán'),
        ),
    ]
