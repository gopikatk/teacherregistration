from django.db import models

class ProductDetails(models.Model):
    firstname=models.CharField(max_length=225,null=True)
    lastname=models.CharField(max_length=225,null=True)
    age=models.CharField(max_length=3,null=True)
    dob=models.DateField(null=True)
    gender=models.CharField(max_length=125,null=True)
    
    department=models.CharField(max_length=255)
    nof=models.CharField(max_length=255)
    nom=models.CharField(max_length=255)
    email=models.CharField(max_length=255,null=True)
    phone=models.CharField(max_length=255,null=True)
    address=models.CharField(max_length=255,null=True)
    image = models.ImageField(upload_to="image/",default='static/images/icon.png',null=True)

    

# Create your models here.

