from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from phongthuy.froms import simphongthuy
from phongthuy.models import Datapt, namsinh, nguhanh
from sanpham.models import SanPham

def diem(request):
    data = Datapt.objects.all()
    data_ns = namsinh.objects.all()
    data_nh = nguhanh.objects.all()

    ngay = request.GET.get('ngay')
    if ngay:
        data = data.filter(
            Q(ngay=ngay)

        )
    thang = request.GET.get('thang')
    if thang:
        data = data.filter(
            Q(thang=thang)

        )
    nam = request.GET.get('namsinh')
    if nam:
        data = data_ns.filter(
            Q(namsinh__icontains=nam)

        )
    menh = request.GET.get('menh')
    if menh:
        data = data_nh.filter(
            Q(name__icontains=menh)

        )
    sp = SanPham.objects.all()
    simnamsinh = request.GET.get('namsinh')
    if simnamsinh:
        sp = sp.filter(
            Q(SoSim__icontains=ngay) and Q(SoSim__icontains=thang) or Q(SoSim__icontains=nam)
        )[0:50]
    pt = {
        'data':data,
        'sp':sp,
        'data_ns':data_ns,
        'ngay':ngay,
        'thang':thang,
        'nam':nam,
        'menh':menh,
    }
    return render(request, 'simso/sub/kiem.html',pt)


