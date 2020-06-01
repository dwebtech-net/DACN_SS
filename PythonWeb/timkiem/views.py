import operator

from django.shortcuts import render
from django.db.models import Q
from sanpham.models import SimTheoGia ,NhaMang, SimTheoLoai , SimNamSinh ,SanPham
from news.models import TinTuc, DanhMucTinTuc

def timkiem_nangcao(request):
    sp = SanPham.objects.filter(DaBan=False)
    nm = NhaMang.objects.all()
    ns = SimNamSinh.objects.all()
    stl = SimTheoLoai.objects.all()
    stg = SimTheoGia.objects.all()
    dmtt1 = DanhMucTinTuc.objects.get(TieuDe='Bạn cần biết')
    bcbs = dmtt1.tintuc_set.order_by('-NgayTao')[0:5]
    dmtt2 = DanhMucTinTuc.objects.get(TieuDe='Tin mới cập nhật')
    tmcns = dmtt2.tintuc_set.order_by('-NgayTao')[0:5]

# tim theo nha mang

    nhamang = request.GET.get('mang')
    if nhamang:
        sp = sp.filter(
            Q(Mang__in=nhamang)

        )

# tim kiem theo nam sinh

    namsinh = request.GET.get('namsinh')
    if namsinh:
        sp = sp.filter(
            Q(NamSinh__in=namsinh)

        )

# tim kiem theo loai sim

    loai = request.GET.get('loai')
    if loai:
        sp = sp.filter(
            Q(LoaiSims__in=loai)

        )
# tim kiem theo muc gia
    mucgia = request.GET.get('gia')
    if mucgia:
        sp = sp.filter(
            Q(LoaiGia__in=mucgia)

        )

# tim theo so simmmm
    sosim = request.GET.get('so')
    if sosim :
        if '*' in sosim:
            sosim = sosim.split('*')
            if sosim[0] != '':
                sp = sp.filter(Q(SoSim__startswith=sosim[0]))
            if sosim[1] != '':
                sp = sp.filter(Q(SoSim__endswith=sosim[1]))
        else:
            if sosim:
                sp = sp.filter(Q(SoSim__icontains=sosim))

    context = {
        "sp": sp,
        "ns": ns,
        "stl": stl,
        "stg": stg,
        "nm": nm,
        "dmtt1": dmtt1,
        "bcbs": bcbs,
        "dmtt2": dmtt2,
        "tmcns": tmcns,

    }
    return render(request, 'includes/timkiem/ketqua-timkiem.html', context)
