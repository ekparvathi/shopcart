from django.db import models

# Create your models here.
class profile(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    Address=models.CharField(max_length=400)
    PIN=models.CharField(max_length=6)
    Phone=models.BigIntegerField()
    Image=models.FileField(upload_to='static/images/',default='default')
     
    def __repr__(self):
        return(self.Name)

class products(models.Model):
    P_Name=models.CharField(max_length=200)
    P_Type=models.CharField(max_length=200)
    P_Model=models.CharField(max_length=50)
    P_Meterial=models.CharField(max_length=200)
    P_Description=models.CharField(max_length=200)
    P_Image=models.FileField(upload_to='static/images/',default='default')
    P_Price=models.DecimalField(max_digits=5,decimal_places=2)
    P_Size=models.CharField(max_length=5)
    P_Color=models.CharField(max_length=50)
    P_Qty=models.BigIntegerField()
    P_Person=models.CharField(max_length=200)

    # def __repr__(self):
    #     return (self.P_Name)

class cart(models.Model):
    prof=models.ForeignKey(profile,on_delete=models.CASCADE)
    prods=models.ForeignKey(products,on_delete=models.CASCADE)
    qty=models.BigIntegerField(default=1)
    price=models.DecimalField(max_digits=5,decimal_places=2,default=0)

    # def __repr__(self):
    #     return f"{self.}"