from django.shortcuts import render,HttpResponse,redirect
from app.models import Contact,Product
from math import ceil
from django.contrib import messages
# Create your views here.
def copy(request):
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n // 4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
    params= {"allProds": allProds}
    return render(request,"app/index.html",params)

def contact(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        description=request.POST.get("desc")
        phone=request.POST.get("phone")
        myquery=Contact(name=name,email=email,desc=description,phone=phone)
        myquery.save()

        messages.info(request,'we will get back soon')
    return render(request,'app/contact.html')

def checkout(request):
    return render(request,'app/checkout.html')