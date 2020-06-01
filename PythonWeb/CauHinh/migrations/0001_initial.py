# Generated by Django 2.2.6 on 2020-06-01 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CauHinhSeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Sim số đẹp - Thương hiệu sim số uy tín nhất việt nam', max_length=200, verbose_name='Tiêu đề website')),
                ('keyword', models.CharField(default='Mua sim ,bán sim , Sim số đẹp, sim tứ quý ,sim năm sinh', help_text='Từ khóa được phân cách bằng dầu phẩy', max_length=300, verbose_name='Từ khóa website')),
                ('des', models.TextField(default='Sim số đẹp - Thương hiệu uy tín trong ngành sim số đẹp từ hơn 10 năm qua, giao sim Miễn phí,dịch vụ tốt nhất thị trường', max_length=300, verbose_name='Mô tả website')),
                ('favico', models.ImageField(default='/favico.png', null=True, upload_to='', verbose_name='Favico')),
                ('google', models.CharField(blank='', default='Mã google site', max_length=100, verbose_name='Google-Webmaster')),
                ('fb_app', models.CharField(blank='', default='123456767890', max_length=100, verbose_name='Facebook app id')),
                ('robots', models.CharField(choices=[('noindex,nofollow', 'Chặn google lập chỉ mục trang web :(noindex,nofollow)'), ('index,follow', 'Lập chỉ mục trang web (index,follow)')], default='index,follow', help_text='Tùy chỉnh lập chỉ mục trang web với google', max_length=100, verbose_name='Robots')),
            ],
            options={
                'verbose_name_plural': 'Cấu Hình SEO',
            },
        ),
        migrations.CreateModel(
            name='CauHinhTrang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Sim số đẹp - Thương hiệu sim số uy tín nhất việt nam', max_length=200, verbose_name='Tiêu đề website')),
                ('sdt1', models.CharField(default='0969641652', max_length=300, verbose_name='Số điện thoại 1')),
                ('sdt2', models.CharField(default='0345003654', max_length=300, verbose_name='Số điện thoại 2')),
                ('banner', models.ImageField(default='/logo_banner.png', null=True, upload_to='', verbose_name='Banner đầu trang')),
                ('zalo', models.CharField(default='0969641652', max_length=300, verbose_name='Nhập số zalo')),
                ('chatfb', models.CharField(default='1317836384978667', max_length=300, verbose_name='Nhập id page facebook')),
                ('footer', models.TextField(default='<p><strong>&copy;Sim HUTECH - Hệ thống phân phối <a href="/">Sim số đẹp</a> lớn nhất Việt Nam! <div></strong></br><a href="http://online.gov.vn/HomePage/CustomWebsiteDisplay.aspx?DocId=3849"><img alt="Sim thăng long đã đăng ký với bộ công thương" src="https://static.simthanglong.vn/images/bct.jpg" style="width: 215px;"></a>', max_length=1000, verbose_name='Thêm nội dung chân trang')),
            ],
            options={
                'verbose_name_plural': 'Cấu Hình Trang',
            },
        ),
    ]
