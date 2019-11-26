# Generated by Django 2.2.6 on 2019-11-25 14:30

import datetime
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('desp', models.TextField(max_length=500, null=True)),
                ('category', models.CharField(blank=True, choices=[('Grocery', 'Grocery'), ('Mobiles', 'Mobiles'), ('Clothes', 'Clothes'), ('Electronics', 'Electronics'), ('Home Appliances', 'Home appliances'), ('Beauty', 'Beauty'), ('Toys', 'Toys'), ('Sports', 'Sports'), ('Footwear', 'Footwear'), ('Others', 'Others')], max_length=50, null=True)),
                ('minimum_price', models.IntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('start', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('end', models.DateTimeField(default=datetime.datetime(2019, 11, 26, 0, 30, 58, 949703, tzinfo=utc))),
                ('current_bid', models.IntegerField(default=0)),
                ('product_sold', models.BooleanField(default=False)),
                ('choose', models.CharField(blank=True, choices=[('Sell', 'Sell'), ('Rent', 'Rent')], max_length=50, null=True)),
                ('rent_status', models.BooleanField(default=False)),
                ('rent_price', models.IntegerField(default=0)),
                ('rent_time_start', models.DateTimeField(null=True)),
                ('rent_time_end', models.DateTimeField(null=True)),
                ('rent_fine', models.IntegerField(default=0)),
            ],
        ),
    ]
