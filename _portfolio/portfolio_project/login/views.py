from django.shortcuts import render
from login.models import REGISTERED_USER_DETAIL
from contest_details.models import contest_detail
from stopstalk.models import stopstalk_detail
from django.contrib import messages
# Create your views here.
def login(request):
    return render(request,'LOGIN/index.html')
def logging_in(request):
    password_entered=request.POST['password']
    try:
        print(password_entered)
        detail_of_user=REGISTERED_USER_DETAIL.objects.get(registered_uesr_password=password_entered)
        contest_detail_of_user=[]
        stopstalk_detail_of_user=[]
        try:
            all_contest_details_in_database=contest_detail.objects.all()
            for a in all_contest_details_in_database:
                if(a.registered_user_password==password_entered):
                    contest_detail_of_user.append(a)
        except:
            pass
        try:
            all_stopstalk_details_in_database=stopstalk_detail.objects.all()
            for a in all_stopstalk_details_in_database:
                if(a.registered_user_password==password_entered):
                    stopstalk_detail_of_user.append(a)
        except:
            pass
        return render(request,'PORTFOLIO/index.html',{"user":detail_of_user,"contest":contest_detail_of_user,"s":stopstalk_detail_of_user})
    except:
        messages.info(request,"Sorry you have entered wrong password!!! try again")
        return render(request,'LOGIN/index.html')
