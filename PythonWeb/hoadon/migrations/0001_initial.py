# Generated by Django 3.0.6 on 2020-06-09 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('giohang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoaDon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HoTenNguoiNhan', models.CharField(default='', max_length=200, verbose_name='Họ tên người nhận')),
                ('DiaChiNguoiNhan', models.TextField(default='', verbose_name='Địa chỉ người nhận')),
                ('SDT', models.CharField(default='', max_length=10, verbose_name='Số điện thoại người nhận')),
                ('NgayDatHang', models.DateTimeField(auto_now_add=True, verbose_name='Ngày đặt hàng')),
                ('ThanhToan', models.BooleanField(default=False, verbose_name='Thanh toán')),
                ('GiaoHang', models.BooleanField(default=False, verbose_name='Giao hàng')),
                ('TongTien', models.FloatField(default=0, verbose_name='Tổng tiền')),
                ('GH', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='giohang.GioHang', verbose_name='Giỏ hàng')),
            ],
            options={
                'verbose_name_plural': 'Hóa đơn',
            },
        ),
    ]
