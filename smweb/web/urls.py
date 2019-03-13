from django.urls import path
from web.menu import menuViews
from web.chart import chartViews
app_name='web'

urlpatterns=[
    path('', menuViews.index, name='index'),
    path('<int:mainmenu_id>/stock',menuViews.stock, name='stock'),
    path('web/chart.html', chartViews.chart, name='chart')
]