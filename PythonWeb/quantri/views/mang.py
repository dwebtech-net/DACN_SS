from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView

from quantri.froms.mang import ThemNhaMangForm
from sanpham.models import NhaMang


@login_required(login_url='/user/dang-nhap')
def Quyen404(request):
    data = {"item": {'title': 'Lỗi truy cập'}}
    return render(request, 'quanly/page/404-user.html', data)


class ThemMang(SuccessMessageMixin,CreateView):
    model = NhaMang
    form_class = ThemNhaMangForm
    template_name = 'quanly/page/mang/them.html'
    success_url = reverse_lazy('quantri:Them-mang')
    success_message = "Cập nhật thành công!"
    paginate_by = 5
    extra_context = {
        'class_tp': 'active',
        'item': 'Thêm nhà mạng'
    }
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['mang'] = NhaMang.objects.order_by('-id')
        return data

# Kiem tra quyen truy cap - Bao nhi
    @method_decorator(login_required(login_url=reverse_lazy('user:dangnhap')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('user:dangnhap')
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            return redirect('quantri:Quyen-truy-cap')
        return super().dispatch(self.request, *args, **kwargs)


@login_required
def SuaMang(request, id):
    obj = get_object_or_404(NhaMang, id=id)
    form = ThemNhaMangForm(request.POST or None, instance=obj)
    context = {'form': form}

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Cập nhật thông tin thành công")
        context = {'form': form}
        return render(request, 'quanly/page/them-san-pham.html', context)

    else:
        context = {'form': form,
                   'error': 'Có gì đó sai sai'}
        return render(request, 'quanly/page/them-san-pham.html', context)

class DanhSachMang(ListView):
    model = NhaMang
    paginate_by = 20  # if pagination is desired
    template_name = 'quanly/page/mang/them.html'
    context_object_name = 'mang'
    extra_context = {
        'title': 'Danh sách sản sim',
        'item' : 'Danh sác sim'
    }

class XoaMang(SuccessMessageMixin,DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công phòng!"
    success_url = reverse_lazy('phong:Danh-sach-phong')
    extra_context = {
        'title': 'Xoá phòng',
        'item': 'Xoá phòng'
    }

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(NhaMang, id=id_)