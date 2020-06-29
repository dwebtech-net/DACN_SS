from gettext import gettext
from django import forms

from DauGia.models import DauGia
from sanpham.models import SanPham, SIM_CHOICES


class ThemSanPhamForm(forms.ModelForm):
    class Meta:
        model = DauGia
        fields = '__all__'
        exclude = ['DuongDan',]
        # labels = {
        # }
        widgets = {
            'luotxem': forms.NumberInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Lượt xem',
                'required': False
            }),
            'DaDauGia': forms.CheckboxInput(attrs={
                'class': 'input input--switch border',
            }),
            'GiaMuaLuon': forms.NumberInput(attrs={
                'class': 'input pr-16 w-full border col-span-4',
                'placeholder': '500000',
                'required': False
            }),
            'GiaToiThieu': forms.NumberInput(attrs={
                'class': 'input pr-16 w-full border col-span-4',
                'placeholder': '500000',
                'required': False
            }),
            'GiaHienTai': forms.NumberInput(attrs={
                'class': 'input pr-16 w-full border col-span-4',
                'placeholder': '500000',
                'required': False
            }),
            'Sim': forms.SelectMultiple(attrs={
                'class': 'select2 w-full',
                'multiple': True,
                'required': False
            }),
            'NguoiDauGiaHienTai': forms.SelectMultiple(attrs={
                'class': 'select2 w-full',
                'required': False
            }),
            'NgayHetHan': forms.DateTimeInput(attrs={
                'class': 'datepicker input pl-12 border',
                'required': False
            }),
        }