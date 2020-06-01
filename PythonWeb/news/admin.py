from django.contrib import admin
from .models import TinTuc,DanhMucTinTuc
from django.utils.safestring import mark_safe

# Register your models here.
class TinTucAdmin(admin.ModelAdmin):
    list_display = [ 'tieu_de', 'mo_ta_ngan', 'anh', 'ngay_tao', 'duong_dan', 'id']
    list_filter = ['ngay_tao']
    search_fields = ['tieu_de']
    exclude = ['duong_dan', ]
    list_per_page = 5

    class Media:
        js = ('tinymce/tinymce.min.js', 'home/js/tinymce_4_config.js')

    def _Noi_dung(self, obj):
        _noi_dung = mark_safe(obj.noi_dung)
        return _noi_dung


admin.site.register(TinTuc,TinTucAdmin)


class DanhMucTinTucAdmin(admin.ModelAdmin):
    list_display = [ 'tieu_de', 'duong_dan', 'id']
    search_fields = ['tieu_de']
    exclude = ['duong_dan', ]
    list_per_page = 5


admin.site.register(DanhMucTinTuc,DanhMucTinTucAdmin)
