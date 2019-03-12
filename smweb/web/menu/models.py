from django.db import models

class Mainmenu(models.Model):
    mainmenuName=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now=True,blank=True)
    address=models.CharField(max_length=200)
    def __str__(self):
        return self.mainmenuName

class Submenu(models.Model):
    mainmenu=models.ForeignKey(Mainmenu,on_delete=models.CASCADE)
    submenuName=models.CharField(max_length=200)

    def __str__(self):
        return self.submenuName