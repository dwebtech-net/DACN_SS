from django.shortcuts import render
from django.db.models import Q
from sanpham.models import SimTheoGia ,NhaMang, SimTheoLoai , SimNamSinh ,SanPham

def timkiem_nangcao(request):
    sp = SanPham.objects.all()
    nm = NhaMang.objects.all()
    ns = SimNamSinh.objects.all()
    stl = SimTheoLoai.objects.all()
    stg = SimTheoGia.objects.all()

# tim theo so simmmm
    sosim = request.GET.get('so')
    if "*" in sosim:
        sosim = sosim.split('*')
        if sosim[0] != '':
            sp = sp.filter(Q(SoSim__startswith=sosim[0]))
        if sosim[1] != '':
            sp = sp.filter(Q(SoSim__endswith=sosim[1]))
        
    else:
        if sosim:
            sp = sp.filter(
                Q(SoSim__iregex=sosim) or Q(SoSim__contains=sosim)
            )
        else:
            sp = sp.filter(
                Q(SoSim__contains=sosim)
            )

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

    context = {
        "sp": sp,
        "ns": ns,
        "stl": stl,
        "stg": stg,
        "nm": nm,

    }
    return render(request, 'includes/timkiem/ketqua-timkiem.html', context)
