from django.db import models
from django.template.defaultfilters import truncatechars
from PythonWeb.utils import get_unique_slug

##
# Chọn sim vip _ thường
##


SIM_CHOICES = (
    ('thuong', 'Sim Thường'),
    ('khuyenmai', 'Sim Khuyến Mãi'),
    ('vip', 'Sim Vip'),
    ('vipdn', 'Sim Vip Doanh Nhân'))

##
# Tạo danh muc san pham _Duc
##
class SimTheoGia(models.Model):
    title = models.CharField(max_length=100,verbose_name='Tiêu đề')

    class Meta:
        verbose_name_plural = 'Sim theo giá'


class NhaMang(models.Model):
    title = models.CharField(max_length=100,verbose_name='Tiêu đề')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Nhà mạng'


class SimTheoLoai(models.Model):
    title = models.CharField(max_length=100,verbose_name='Tiêu đề')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sim theo loại'


class SimNamSinh(models.Model):
    title = models.CharField(max_length=100,verbose_name='Tiêu đề')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sim năm sinh'


# Tạo bảng sản phẩm

class SanPham(models.Model):
    LoaiSims = models.ManyToManyField(SimTheoLoai, blank=True,default=0,verbose_name='Loại sim')
    slug = models.SlugField(max_length=20,null=False,default='')
    TacVu = models.CharField(max_length=100,choices=SIM_CHOICES,default='thuong',verbose_name='Tác vụ trang chủ')
    SoSim = models.CharField(max_length=100,verbose_name='Nhập số sim')
    Gia = models.IntegerField(default=0,verbose_name='Nhập giá bán')
    Mang = models.ForeignKey(NhaMang, on_delete=models.CASCADE, null=True,verbose_name='Nhà Mạng')
    Anh = models.ImageField(null=True,verbose_name='Hình đại diện')
    NgayNhap = models.DateTimeField(auto_now_add=True,verbose_name='Ngày nhập')

    def __str__(self):
        return self.SoSim

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'SoSim', 'slug')
        super().save(*args, **kwargs)

    # def get_loaisims(self):
    #     return " - ".join([s.title for s in self.LoaiSims.all()])

    class Meta:
        verbose_name_plural = 'Sản Phẩm'


