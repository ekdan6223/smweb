from django.shortcuts import render,get_object_or_404
from web.menu.models import Mainmenu,Submenu
# Create your views here.

def index(request):
    mainQuestion_Name_list=Mainmenu.objects.all()[:10]
    context ={'mainQuestion_Name_list':mainQuestion_Name_list}
    return render(request,'web/index.html',context)

def menu(request,mainmenuName_id):
    mainmenu=get_object_or_404(Mainmenu,pk=mainmenuName_id)
    return render(request,'web/menu.html',{'mainmenu':mainmenu})
