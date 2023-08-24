from django.shortcuts import render,redirect,HttpResponse
from  django.conf import settings
from .models import Contact



# Create your views here.
def index(request):
    if request.method=="POST":
        usn=request.POST.get('usn','')
        name=request.POST.get('name','')
        sem=request.POST.get('sem','')
        phno=request.POST.get('phno','')
        email=request.POST.get('email','')
        if usn and name and sem and phno and email:
            contact=Contact(usn=usn,name=name,sem=sem,phno=phno,email=email)
            contact.save()
        else:
            return HttpResponse("registered successfully")
    return render(request,'index.html')
