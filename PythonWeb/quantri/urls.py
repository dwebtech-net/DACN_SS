from django.urls import path

from quantri.views.main import *

app_name = 'quantri'
urlpatterns = [
    path('', main, name='main'),
]
