from django.urls import path
from . import views

app_name = 'tintuc'
urlpatterns = [
    path('', views.home, name='news'),
    path("xem-danh-muc-tin-tuc/<str:DuongDan>/", views.danhmuctintuc, name='danhmuctintuc'),
    path("xem-tin-tuc/<str:DuongDan>/", views.tintuc, name='tintuc'),
]
