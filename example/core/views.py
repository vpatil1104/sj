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
    return render(request,'contact.html')
    #return HttpResponse("th