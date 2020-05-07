from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'LOGIN/index.html')
def logging_in(request):
    print(request.POST['password'])
    return render(request,'PORTFOLIO/index.html')
