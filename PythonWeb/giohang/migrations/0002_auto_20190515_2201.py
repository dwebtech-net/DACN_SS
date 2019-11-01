# Generated by Django 2.2 on 2019-05-15 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sanpham', '0002_auto_20190428_0042'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('giohang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CTGH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SoLuong', models.IntegerField(default=1)),
                ('DonGia', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='GioHang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TongTien', models.FloatField(default=0)),
                ('NgayDatHang', models.DateTimeField(auto_now_add=True)),
                ('ThanhToan', models.BooleanField(default=False)),
                ('MaKH', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('SanPhams', models.ManyToManyField(blank=True, to='sanpham.SanPham')),
            ],
        ),
        migrations.DeleteModel(
            name='CTHD',
        ),
        migrations.DeleteModel(
            name='HoaDon',
        ),
        migrations.AddField(
            model_name='ctgh',
            name='MaHD',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='giohang.GioHang'),
        ),
        migrations.AddField(
            model_name='ctgh',
            name='MaSP',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sanpham.SanPham'),
        ),
    ]
