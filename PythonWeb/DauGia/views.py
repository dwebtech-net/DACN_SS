from django.shortcuts import render, redirect
from sanpham.models import SimNamSinh, SimTheoGia, SimTheoLoai, NhaMang
from hoadon.models import HoaDon
import operator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date
from .models import DauGia

# Create your views here.
def home(request):
    # Lấy dữ liệu từ database
    daugia = DauGia.objects.filter(NgayHetHan__gte=date.today())#.order_by('-NgayHetHan')
    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]

    stg_dsx = sorted(stg, key=operator.attrgetter('title'))
    
    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(daugia, 12)
    try:
        DauGias = paginator.page(page)
    except PageNotAnInteger:
        DauGias = paginator.page(1)
    except EmptyPage:
        DauGias = paginator.page(paginator.num_pages)

    Data = {
            "daugia": DauGias,
            "stl": stl,
            "sns": sns,
            "nm": nm,
            "stg": stg_dsx,
            "hd": hd,
            }
    return render(request, 'simso/page-daugia/list-daugia.html', Data)

def chitietdaugia(request, DuongDan):
    if request.user.is_authenticated == False:
        return redirect('/user/dang-nhap/')
    # Lấy dữ liệu từ database
    daugia = DauGia.objects.get(DuongDan=DuongDan, NgayHetHan__gte=date.today())

    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]
    message = ""

    if request.method == 'POST':
        daugia = DauGia.objects.filter(DuongDan=request.POST.get('DuongDan'))[0]
        if (float)(request.POST.get('GiaDauGia')) > daugia.GiaHienTai:
            daugia.GiaHienTai = request.POST.get('GiaDauGia')
            daugia.NguoiDauGiaHienTai = request.user
            daugia.save()
            return redirect('DauGia:chitietdaugia', daugia.DuongDan)
        else:
            message = "Giá đấu giá nhỏ hơn giá hiện tại"

    Data = {'daugia': daugia,
            "hd": hd,
            "stl": stl,
            "sns": sns,
            "nm": nm,
            "msg": message,
            }
    return render(request, 'simso/page-daugia/detail-daugia.html', Data)

def mualuon(request, DuongDan):
    if request.method == 'POST':
        daugia = DauGia.objects.filter(DuongDan=request.POST.get('DuongDan'))[0]
        daugia.GiaHienTai = daugia.GiaMuaLuon
        daugia.NguoiDauGiaHienTai = request.user
        daugia.DaDauGia = True
        daugia.save()
        return redirect('DauGia:chitietdaugia', daugia.DuongDan)
