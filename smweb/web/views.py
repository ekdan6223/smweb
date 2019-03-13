from django.shortcuts import render,get_object_or_404
from web.menu.models import Mainmenu,Submenu,Product
from django.http import HttpResponseRedirect
from django.urls import  reverse
# Create your views here.

def index(request):
    mainMenu_Name_list=Mainmenu.objects.all()[:10]
    subMenu_Name_list=Submenu.objects.all()[:10]
    prodouct_list=Product.objects.all()[:10]
    context ={'mainMenu_Name_list':mainMenu_Name_list,'subMenu_Name_list':subMenu_Name_list,'product_list':prodouct_list}
    return render(request,'web/index.html',context)

def stock(request,mainmenuName_id):
    mainmenu=get_object_or_404(Mainmenu,pk=mainmenuName_id)
    return render(request,'web/stock.html',{'mainmenu':mainmenu})

def chart(request):
    return render(request,'web/chart.html')