from django.contrib import admin
from .models import SanPham, SimNamSinh, SimTheoGia, SimTheoLoai, NhaMang
from import_export import resources, fields, widgets
from import_export.admin import ImportExportModelAdmin, ExportActionMixin


# Register your models here.


################--Xuất nhập khẩu--#######################

class Sim_Key(resources.ModelResource):
    class Meta:
        skip_unchanged = True
        report_skipped = True
        model = SanPham
        exclude = ['NgayNhap', 'slug', ]
        import_preview = (
            'id', 'LoaiSims__title', 'slug', 'TacVu', 'SoSim', 'Gia', 'Mang__title', 'LoaiGia__title', 'NamSinh',
            'Anh',)
        fields = (
        'id', 'LoaiSims__title', 'slug', 'TacVu', 'SoSim', 'Gia', 'Mang__title', 'LoaiGia__title', 'NamSinh',
        'Anh',)

class Sim(ImportExportModelAdmin,ExportActionMixin):
    list_per_page = 20
    resource_class = Sim_Key
admin.site.register(SanPham, Sim)


# Hiển thị bảng nhà mạng
class NhaMangAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'slug']
    search_fields = ['title']
    exclude = ['slug', ]
    list_per_page = 5


# Hiển thị bảng Sim theo loại
class LoaiSimResource(resources.ModelResource):
    class Meta:
        model = SimTheoLoai
        exclude = ('slug')
        fields = ('id', 'title')
class LoaiSimAdmin(ImportExportModelAdmin):
    list_per_page = 5
    resource_class = LoaiSimResource


admin.site.register(SimTheoLoai, LoaiSimAdmin)


# Hiển thị bảng Sim theo giá
class SimTheoGiaAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'slug')
    search_fields = ['title']
    exclude = ['slug', ]
    list_per_page = 5


# Hiển thị bảng Sim theo năm
class SimTheoNamAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'slug')
    list_per_page = 5


admin.site.register(NhaMang, NhaMangAdmin)
admin.site.register(SimTheoGia, SimTheoGiaAdmin)
admin.site.register(SimNamSinh, SimTheoNamAdmin)
