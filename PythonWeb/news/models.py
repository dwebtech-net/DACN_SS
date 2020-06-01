from django.db import models
from PythonWeb.utils import get_unique_slug


# Create your models here.

#Tạo bảng danh mục tin tức
class DanhMucTinTuc(models.Model):
    tieu_de = models.CharField(max_length=500 ,null=True, verbose_name='Tên danh mục tin tức')
    duong_dan = models.SlugField(max_length=100, null=False, default='', verbose_name='Đường dẫn')

    def __str__(self):
        return self.tieu_de

    def save(self, *args, **kwargs):
        if not self.duong_dan:
            self.duong_dan = get_unique_slug(self, 'tieu_de', 'duong_dan')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Danh mục tin tức'

# Tạo bảng tin tức
class TinTuc(models.Model):
    tieu_de = models.TextField(null=True, verbose_name='Tiêu đề')
    mo_ta_ngan = models.TextField(null=True, verbose_name='Mô tả ngắn')
    noi_dung = models.TextField(null=True, verbose_name='Nội dung')
    anh = models.ImageField(default='product-default.jpg', verbose_name='Ảnh')
    ngay_tao = models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')
    duong_dan = models.SlugField(max_length=200, null=False, default='', verbose_name='Đường dẫn')

    def __str__(self):
        return self.tieu_de

    def save(self, *args, **kwargs):
        if not self.duong_dan:
            self.duong_dan = get_unique_slug(self, 'tieu_de', 'duong_dan')
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Tin tức'


