# Generated by Django 2.2.8 on 2020-06-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DauGia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='daugia',
            name='GiaToiThieu',
            field=models.FloatField(default=0, verbose_name='Giá tối thiểu'),
        ),
    ]