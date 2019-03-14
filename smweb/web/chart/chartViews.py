from django.shortcuts import render,get_object_or_404,render_to_response
from web.menu.models import Mainmenu,Submenu,Product
from django.http import HttpResponseRedirect
from django.urls import  reverse
import random
import datetime
import time

def chart(request):
    mainMenu_Name_list=Mainmenu.objects.all()[:10]
    subMenu_Name_list=Submenu.objects.all()[:10]
    prodouct_list=Product.objects.all()[:10]
    context ={'mainMenu_Name_list':mainMenu_Name_list,'subMenu_Name_list':subMenu_Name_list,'product_list':prodouct_list}
    return render(request, 'web/chart.html', context)

