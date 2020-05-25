# Generated by Django 3.0 on 2020-05-25 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phongthuy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='nguhanh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Tên ngũ hành')),
                ('tuongsinh', models.CharField(max_length=100, verbose_name='Tương sinh')),
                ('tuongkhac', models.CharField(max_length=100, verbose_name='Tương khắc')),
            ],
            options={
                'verbose_name_plural': 'Ngũ hành',
            },
        ),
        migrations.CreateModel(
            name='namsinh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4, unique=True, verbose_name='Năm sinh')),
                ('nguhanh_ns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phongthuy.nguhanh', verbose_name='Thuộc mệnh')),
            ],
        ),
    ]