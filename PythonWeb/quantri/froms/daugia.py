from gettext import gettext
from django import forms
from django.forms import DateTimeField

from DauGia.models import DauGia
from sanpham.models import SanPham, SIM_CHOICES


class ThemDauGiaForm(forms.ModelForm):
    class Meta:
        model = DauGia
        fields = '__all__'
        exclude = ['DuongDan','GiaHienTai','NguoiDauGiaHienTai']
        # labels = {
        # }
        # NgayHetHan = DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S"])
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
            # 'GiaHienTai': forms.NumberInput(attrs={
            #     'class': 'input pr-16 w-full border col-span-4',
            #     'placeholder': '500000',
            #     'required': False
            # }),
            'Sim': forms.Select(attrs={
                'class': 'select2 w-full',
                'multiple': False,
                'required': False
            }),
            # 'NguoiDauGiaHienTai': forms.SelectMultiple(attrs={
            #     'class': 'select2 w-full',
            #     'required': False
            # }),
            'NgayHetHan': forms.DateTimeInput(attrs={
                'class': 'input w-56 border block mx-auto',
                'required': False,
                'data-timepicker': 'true',
                'type': 'datetime-local'
            }),
        }