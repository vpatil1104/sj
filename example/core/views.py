from django.shortcuts import render
from core.models import Contact
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is home page")

def contact(request):
    if request.method =='POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        usertype = request.POST.get('usertype')
        contact=Contact(name=name,password=password,usertype=usertype,date=datetime.today())
        contact.save()
        
    elif request.method =='POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
       
        contact=Contact(name=name,password=password,date=datetime.today())
        contact.save()
    return render(request,'contact.html')
    #return HttpResponse("th
    
def Home(request):
    return render(request,'Home.html')

def wallect(request):
    return render(request,'wallect.html')

def send_money(request):
    if request.method =='POST':
        name = request.POST.get('name')
        Amount= request.POST.get('Amount')
        send_money=send_money(name=name,Amount=Amount,date=datetime.today())
        send_money.save()
    return render(request,'send_money.html')

def request_money(request):
    return render(request,'Request_Money.html')

def request_recived(request):
    return render(request,'Request_Received.html')

def logout(request):
    return render(request,'logout.html')
