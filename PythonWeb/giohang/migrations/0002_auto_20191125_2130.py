# Generated by Django 2.2.6 on 2019-11-25 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sanpham', '0001_initial'),
        ('giohang', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctgh',
            name='GH',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='giohang.GioHang'),
        ),
        migrations.AddField(
            model_name='ctgh',
            name='SP',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sanpham.SanPham'),
        ),
        migrations.AddField(
            model_name='giohang',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
