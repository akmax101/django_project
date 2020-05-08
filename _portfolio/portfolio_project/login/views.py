from django.shortcuts import render
from login.models import REGISTERED_USER_DETAIL
from django.contrib import messages
# Create your views here.
def login(request):
    return render(request,'LOGIN/index.html')
def logging_in(request):
    password_entered=request.POST['password']
    try:
        print(password_entered)
        detail_of_user=REGISTERED_USER_DETAIL.objects.get(registered_uesr_password=password_entered)
        print(detail_of_user.registered_uesr_bio)
        return render(request,'PORTFOLIO/index.html',{"user":detail_of_user})
    except:
        messages.info(request,"Sorry you have entered wrong password!!! try again")
        return render(request,'LOGIN/index.html')
