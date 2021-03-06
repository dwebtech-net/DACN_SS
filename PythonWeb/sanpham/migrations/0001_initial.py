# Generated by Django 3.0.6 on 2020-06-09 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NhaMang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Tiêu đề')),
                ('slug', models.SlugField(default='', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Nhà mạng',
            },
        ),
        migrations.CreateModel(
            name='SimNamSinh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Tiêu đề')),
                ('slug', models.SlugField(default='', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Sim năm sinh',
            },
        ),
        migrations.CreateModel(
            name='SimTheoGia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Tiêu đề')),
                ('slug', models.SlugField(default='', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Sim theo giá',
            },
        ),
        migrations.CreateModel(
            name='SimTheoLoai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Tiêu đề')),
                ('slug', models.SlugField(default='', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Sim theo loại',
            },
        ),
        migrations.CreateModel(
            name='SanPham',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='', max_length=100)),
                ('TacVu', models.CharField(choices=[('khuyenmai', 'Khuyến Mãi'), ('thuong', 'Sim Thường'), ('vip', 'Sim Vip'), ('vipdn', 'Sim Vip Doanh Nhân')], default='thuong', max_length=100, verbose_name='Tác vụ trang chủ')),
                ('SoSim', models.CharField(max_length=100, unique=True, verbose_name='Số sim')),
                ('Gia', models.IntegerField(verbose_name='Giá bán')),
                ('NgayNhap', models.DateTimeField(auto_now_add=True, verbose_name='Ngày nhập')),
                ('DaBan', models.BooleanField(default=False, verbose_name='Đã bán')),
                ('LoaiGia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sanpham.SimTheoGia', verbose_name='Sim theo giá ')),
                ('LoaiSims', models.ManyToManyField(default=0, to='sanpham.SimTheoLoai', verbose_name='Loại sim')),
                ('Mang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sanpham.NhaMang', verbose_name='Nhà Mạng')),
                ('NamSinh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sanpham.SimNamSinh', verbose_name='Theo năm sinh ')),
            ],
            options={
                'verbose_name_plural': 'Sản Phẩm',
            },
        ),
    ]
