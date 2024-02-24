# from django.db import models
# import datetime 
# import os

# def getFileName(request,filename):
#     now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
#     new_filename="%s%s"%(now_time,filename)
#     return os.path.join('uploads/',new_filename)

# # Create your models here.
# class Catagory(models.Model):
#     name=models.CharField(max_length=150,null=False,blank=False)
#     image=models.ImageField(upload_to=getFileName,null=True,blank=True)
#     description=models.TextField(max_length=500,null=False,blank=False)
#     status=models.BooleanField(default=False,help_text="0-show,1-hidden")
#     created_at=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

#     # def __str__(self):
#     #     return self.name
# class Product(models.Model):
#     category=models.ForeignKey(Catagory,on_delete=models.CASCADE)
#     name=models.CharField(max_length=150,null=False,blank=False)
#     vendor=models.CharField(max_length=150,null=False,blank=False)
#     product_image=models.ImageField(max_length=150,default=0,upload_to=getFileName,null=True,blank=True)
#     quantity=models.IntegerField(default=0,null=False,blank=False)
#     original_price=models.IntegerField(default=0,null=False,blank=False)
#     selling_price=models.IntegerField(default=0,null=False,blank=False)
#     description=models.TextField(max_length=500,null=False,blank=False)
#     status=models.BooleanField(default=False,help_text="0-show,1-hidden")
#     trending=models.BooleanField(default=False,help_text="0-default,1-trending")
#     created_at=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

from django.db import models
# from django.contrib.auth.models import User
import datetime
import os

def getFileName(requset,filename):
  now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('uploads/',new_filename)

class Catagory(models.Model):
  name=models.CharField(max_length=150,null=False,blank=False)
  image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  description=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  created_at=models.DateTimeField(auto_now_add=True)

  def __str__(self) :
    return self.name

class Product(models.Model):
  category=models.ForeignKey(Catagory,on_delete=models.CASCADE)
  name=models.CharField(max_length=150,null=False,blank=False)
  vendor=models.CharField(max_length=150,default=0,null=False,blank=False)
  product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  quantity=models.IntegerField(default=0,null=False,blank=False)
  original_price=models.IntegerField(default=0,null=False,blank=False)
  selling_price=models.FloatField(default=0,null=False,blank=False)
  description=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
  created_at=models.DateTimeField(auto_now_add=True)

  def __str__(self) :
    return self.name
