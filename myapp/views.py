from django.http import HttpResponse
from django.shortcuts import render, redirect

from myapp.models import Studentdb, Registerdb, Imagedb


# Create your views here.
def index(request):
    return HttpResponse("Hai")

def sample(request):
    return HttpResponse("<h1>sample</h1>")

def samplepage(request):
    return render(request,"sample.html")

def homepage(request):
    return render(request,"home.html")

def reg(request):
    return render(request,"reg.html")

def student(request):
    return render(request,"student.html")

def savedata(request):
    if request.method=="POST":
        na=request.POST.get("fname")
        num=request.POST.get("mob")
        # object for db Studentdb
        obj=Studentdb(Name=na,Mobile=num)
        obj.save()
        return redirect(reg)

def register(request):
    return render(request,"registeration.html")
def registersave(request):
    if request.method=="POST":
        na=request.POST.get("fname")
        ag=request.POST.get("age")
        mo=request.POST.get("mob")
        ad=request.POST.get("address")
        obj=Registerdb(Name=na,Age=ag,Mobile=mo,Address=ad)
        obj.save()
        return redirect(register)

def imagesave(request):
    if request.method=="POST":
        na = request.POST.get("fname")
        pic=request.FILES["pic"]
        obj=Imagedb(Name=na,Image=pic)
        obj.save()
        return redirect(imagesave)
    return render(request,"ImageReg.html")

