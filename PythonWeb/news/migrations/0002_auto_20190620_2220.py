# Generated by Django 2.2 on 2019-06-20 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tintuc',
            name='CoverImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
