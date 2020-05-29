from django.contrib import admin
from .models import HoaDon

# Register your models here.

# Hiển thị hóa đơn trên trang admin
class HoaDonAdmin(admin.ModelAdmin):
    list_display = ['GH', 'NgayDatHang', 'TongTien', 'ThanhToan', 'GiaoHang','Nguoi_mua', 'id', ]
    list_filter = ['id']
    search_fields = ['GH']
    list_per_page = 10

    def Nguoi_mua(self, obj):
        return obj.GH.user.HoTen()

    Nguoi_mua.short_description = "Người mua"

admin.site.register(HoaDon, HoaDonAdmin)

