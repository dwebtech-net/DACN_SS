from django.db.models import Max
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from .models import SanPham, SimTheoLoai, SimNamSinh, NhaMang, SimTheoGia
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from giohang.models import GioHang, CTGH
from user.models import CustomerUser
from news.models import TinTuc, DanhMucTinTuc
from hoadon.models import HoaDon
import operator

# Create your views here.
def index(request):
    # Lấy dữ liệu từ database
    km = SanPham.objects.filter(TacVu='khuyenmai', DaBan=False)[0:12]
    vip = SanPham.objects.filter(TacVu='vip', DaBan=False)[0:9]
    vipdn = SanPham.objects.filter(TacVu='vipdn', DaBan=False)[0:9]
    thuong = SanPham.objects.filter(TacVu='thuong', DaBan=False)[0:999]

    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]


    Data = {
            "hd": hd,
            "km": km,
            "vip": vip,
            "vipdn": vipdn,
            "thuong": thuong,
            "stl": stl,
            "sns": sns,
            "nm": nm,
            "stg": stg,
            }
    return render(request, "simso/index.html", Data)

def sanpham(request, slug):
    # Lấy dữ liệu từ database
    sanpham = SanPham.objects.get(slug=slug, DaBan=False)

    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]

    Data = {'sanpham': sanpham,
            "hd": hd,
            "stl": stl,
            "sns": sns,
            "nm": nm,
            }
    return render(request, 'simso/detail-sim/detail-sim.html', Data)

def error(request):
    return render(request, 'simso/page-user/error.html')


def simtheogia(request, slug):

    stg1 = SimTheoGia.objects.get(slug=slug)
    sanpham = stg1.sanpham_set.filter(DaBan=False)
    paginator = Paginator(sanpham, 25)  # Show 25 contacts per page
    page = request.GET.get('page')
    sanphams = paginator.get_page(page)

    stl = SimTheoLoai.objects.order_by('?')
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]

    Data = {
            'stg1': stg1,
            'sanpham': sanphams,
            "hd": hd,
            "stl": stl,
            "sns": sns,
            "nm": nm,
            }
    return render(request, 'simso/category/sim-theo-gia.html', Data)


def simtheomang(request, slug):

    nm1 = NhaMang.objects.get(slug=slug)
    sanpham = nm1.sanpham_set.filter(DaBan=False)

    paginator = Paginator(sanpham, 70)  # Show 25 contacts per page

    page = request.GET.get('page')
    sanphams = paginator.get_page(page)
    stl = SimTheoLoai.objects.order_by('?')
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]
    Data = {
            'nm1': nm1,
            'sanpham': sanphams,
            "hd": hd,
            "stl": stl,
            "sns": sns,
            "nm": nm,
            "stg": stg,
            }
    return render(request, 'category/sim-theo-mang.html', Data)

def simtheoloai(request, slug):
    stl1 = SimTheoLoai.objects.get(slug=slug)

    sanpham = stl1.sanpham_set.filter(DaBan=False)
    paginator = Paginator(sanpham, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    sanphams = paginator.get_page(page)

    stl = SimTheoLoai.objects.order_by('?')
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]

    Data = {
            'stl1': stl1,
            'sanpham': sanphams,
            "hd": hd,
            "stl": stl,
            "sns": sns,
            "nm": nm,
            "stg": stg,

            }
    return render(request, 'category/sim-theo-loai.html', Data)


def simnamsinh(request, slug):

    sns1 = SimNamSinh.objects.get(slug=slug)
    sanpham = sns1.sanpham_set.filter(DaBan=False)

    paginator = Paginator(sanpham, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    sanphams = paginator.get_page(page)

    stl = SimTheoLoai.objects.order_by('?')
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]


    Data = {
            'sns1': sns1,
            'sanpham': sanphams,
            "hd": hd,
            "stl": stl,
            "sns": sns,
            "nm": nm,
            "stg": stg,
            }
    return render(request, 'simso/category/sim-nam-sinh.html', Data)


def tknc(request, slug):
    sp = SanPham.objects.get(slug=slug, DaBan=False)
    Data = {
            'sp':sp,
            }
    return render(request, 'includes/timkiem/timkiem-nangcao.html', Data)

