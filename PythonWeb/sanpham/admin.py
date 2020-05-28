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
        'id', 'LoaiSims', 'slug', 'TacVu', 'SoSim', 'Gia', 'Mang', 'LoaiGia', 'NamSinh',
        'Anh',)

class Sim(ImportExportModelAdmin,ExportActionMixin):
    exclude = ('LoaiGia',)
    list_per_page = 20
    resource_class = Sim_Key
    def save_model(self, request, obj, form, change):
        gia = obj.Gia

        if gia < 500000:
            loaigia_obj = SimTheoGia.objects.filter(title="Sim dưới 500 nghìn").last()
            if loaigia_obj:
                obj.LoaiGia = loaigia_obj
            else:
                loaigia_obj = SimTheoGia.objects.filter(title="Giá khác").last()
                obj.LoaiGia = loaigia_obj
        elif gia > 500000 & gia < 1000000:
            loaigia_obj = SimTheoGia.objects.filter(title="Sim giá 500 - 1 triệu").last()
            if loaigia_obj:
                obj.LoaiGia = loaigia_obj
            else:
                loaigia_obj = SimTheoGia.objects.filter(title="Giá khác").last()
                obj.LoaiGia = loaigia_obj
        elif gia > 1000000 & gia < 3000000:
            loaigia_obj = SimTheoGia.objects.filter(title="Sim giá 1 triệu - 3 triệu").last()
            if loaigia_obj:
                obj.LoaiGia = loaigia_obj
            else:
                loaigia_obj = SimTheoGia.objects.filter(title="Giá khác").last()
                obj.LoaiGia = loaigia_obj
        elif gia > 3000000 & gia < 5000000:
            loaigia_obj = SimTheoGia.objects.filter(title="Sim giá 3 triệu - 5 triệu").last()
            if loaigia_obj:
                obj.LoaiGia = loaigia_obj
            else:
                loaigia_obj = SimTheoGia.objects.filter(title="Giá khác").last()
                obj.LoaiGia = loaigia_obj
        elif gia > 5000000 & gia < 10000000:
            loaigia_obj = SimTheoGia.objects.filter(title="Sim giá 5 triệu - 10 triệu").last()
            if loaigia_obj:
                obj.LoaiGia = loaigia_obj
            else:
                loaigia_obj = SimTheoGia.objects.filter(title="Giá khác").last()
                obj.LoaiGia = loaigia_obj
        elif gia > 10000000 & gia < 50000000:
            loaigia_obj = SimTheoGia.objects.filter(title="Sim giá 10 triệu - 50 triệu").last()
            if loaigia_obj:
                obj.LoaiGia = loaigia_obj
            else:
                loaigia_obj = SimTheoGia.objects.filter(title="Giá khác").last()
                obj.LoaiGia = loaigia_obj
        obj.save()
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
    exclude = ('slug',)
    search_fields = ['title']
    list_per_page = 5


# Hiển thị bảng Sim theo năm
# Hiển thị bảng Sim theo loại
class SimNamSinhResource(resources.ModelResource):
    class Meta:
        model = SimNamSinh
        exclude = ('slug')
        fields = ('id', 'title')
class SimTheoNamAdmin(ImportExportModelAdmin):
    list_per_page = 5
    resource_class = SimNamSinhResource

admin.site.register(NhaMang, NhaMangAdmin)
admin.site.register(SimTheoGia, SimTheoGiaAdmin)
admin.site.register(SimNamSinh, SimTheoNamAdmin)
