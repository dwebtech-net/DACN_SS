from django.urls import path, re_path
from quantri.views.donhang import *
from quantri.views.loaisim import *
from quantri.views.main import *
from quantri.views.mang import *
from quantri.views.sanpham import *
from quantri.views.cauhinh import *

app_name = 'quantri'
urlpatterns = [
    path('', main, name='main'),
    path('error', Quyen404, name='Quyen-truy-cap'),

    # san pham
    path('sanpham/them',ThemSanPham.as_view(),name='Them-san-pham'),
    path('sanpham/sua/<id>',SuaSanPham,name='Sua-san-pham'),
    path('sanpham/danh-sach',DanhSachSanPham.as_view(),name='Danh-sach-san-pham'),

    # nha mang
    path('mang/them/',ThemMang.as_view(),name='Them-mang'),
    path('mang/them/<id>',Suamang,name='Sua-mang'),

    # loai sim
    path('loai/them/',ThemLoaiSim.as_view(),name='Them-loai'),
    path('loai/them/<id>',Sualoaisim,name='Sua-loai'),

    #cau hinh
    path('cau-hinh/cau-hinh-trang/',SuaCauHinhTrang,name='cau-hinh-trang'),
    path('cau-hinh/cau-hinh-seo/',SuaCauHinhSEO,name='cau-hinh-seo'),

    #don hang
    path('donhang',DanhSachDonHang.as_view(),name='danh-sach-don-hang'),
    path('donhang/<id>',UpdateDonHang,name='cap-nhat-don-hang'),
    path('donhang/<id>',XoaDonHang.as_view(),name='cap-nhat-don-hang'),
]
