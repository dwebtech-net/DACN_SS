from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required(login_url='/tai-khoan/dang-nhap')
def main(request):
    # user = request.user.is_superuser
    # # if user == True:
    # #
    # # else:
   return render(request ,'quanly/main.html')