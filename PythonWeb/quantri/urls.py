from django.urls import path, re_path
from quantri.views.loaisim import *
from quantri.views.main import *
from quantri.views.mang import *
from quantri.views.sanpham import *

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
]
