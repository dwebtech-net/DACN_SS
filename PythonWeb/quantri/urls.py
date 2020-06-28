from django.urls import path, re_path
from quantri.views.loaisim import *
from quantri.views.main import *
from quantri.views.mang import *
from quantri.views.sanpham import *
from quantri.views.cauhinh import *
from quantri.views.tintuc import *

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

    #tin tuc
    path('tin-tuc/danh-sach-loai-tin-tuc/',DanhSachLoaiTinTuc.as_view(),name='danh-sach-loai-tin-tuc'),
    path('tin-tuc/danh-sach-loai-tin-tuc/them-moi/',ThemLoaiTinTuc.as_view(),name='them-loai-tin-tuc'),
    path('tin-tuc/danh-sach-loai-tin-tuc/sua/<id>',SuaLoaiTinTuc,name='sua-loai-tin-tuc'),

    path('tin-tuc/danh-sach-tin-tuc/',DanhSachTinTuc.as_view(),name='danh-sach-tin-tuc'),
    path('tin-tuc/danh-sach-tin-tuc/them-moi/',ThemTinTuc.as_view(),name='them-tin-tuc'),
    path('tin-tuc/danh-sach-tin-tuc/sua/<id>',SuaTinTuc,name='sua-tin-tuc'),
]
