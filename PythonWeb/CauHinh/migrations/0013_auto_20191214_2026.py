# Generated by Django 2.2.2 on 2019-12-14 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CauHinh', '0012_cauhinhtrang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cauhinhtrang',
            name='banner',
            field=models.ImageField(default='/logo_banner.png', null=True, upload_to='', verbose_name='Banner đầu trang'),
        ),
        migrations.AlterField(
            model_name='cauhinhtrang',
            name='chatfb',
            field=models.CharField(default='1317836384978667', max_length=300, verbose_name='Nhập id page facebook'),
        ),
    ]
