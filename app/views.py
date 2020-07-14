from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import StudentModel

def admin_login(request):
    return render(request, "admin_login.html")

def admin_check(request):
    un = request.POST.get("t1")
    pa = request.POST.get("t2")

    if un== "umashankar" and pa == "umashankar":
        return redirect('admin_page')
    else:
        mes = messages.error(request,"Invalid Admin")
        return redirect('admin_login',mes)


def admin_page(request):
    return render(request,"admin_page.html")


def new_class(request):
    return render(request,"new_class.html")


def save_data(request,mes):
    na = request.POST.get("p1")
    fly = request.POST.get("p2")
    da = request.POST.get("p3")
    time = request.POST.get("p4")
    fee = request.POST.get("p5")
    dur = request.POST.get("p6")

    StudentModel(name=na,faculty=fly,date=da,time=time,fee=fee,Duration=dur).save()
    mes = messages.add_message("Data Saved")
    return redirect('new_class')