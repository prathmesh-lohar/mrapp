import email
from email.policy import default
from msilib.schema import File
import profile
from time import time
from unicodedata import category
from unittest import result
from urllib import request
from django.db import models
import datetime


from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
import os

from django.forms import CharField, URLField
import urllib3
# Create your models here.

class mr_user(models.Model):
    
    user_name = models.CharField(max_length=255 , default="" ,unique=True)
    
    password = models.CharField(max_length=500, default="")
    
    profile_pic = models.ImageField(upload_to="profiles" , null=True,  blank=True)
    
    first_name = models.CharField(max_length=255, default="")
    
    last_name = models.CharField(max_length=255, default="")
    
    mobile = models.BigIntegerField()
    
    
    dob= models.DateField()

    status = models.CharField(max_length=255, default="Active")

    def __str__(self):
        return self.user_name
    
    
class dr_user(models.Model):
    
    first_name = models.CharField(max_length=255, default="")
    
    last_name = models.CharField(max_length=255, default="")

    # dr_fullname = models.CharField(max_length=255, default="")
    
    hospital_name = models.CharField(max_length=255, default="")
    
    mobile = models.BigIntegerField()
    
    email = models.CharField(max_length=255 , default="" ,unique=True)

    dob= models.DateField()

    category = models.CharField(max_length=255, default="")
 
    latitude = models.FloatField(default=0)
    
    longitude = models.FloatField(default=0)
    
    profile_pic = models.ImageField(upload_to="profiles")
    
    city = models.CharField(max_length=255)
    
    mr_username = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.first_name
    
    
    
    

class visit(models.Model):

    hospital_name = models.CharField(max_length=255)

    doctor_first_name = models.CharField(max_length=255)

    doctor_last_name = models.CharField(max_length=255)

    latitude = models.FloatField(default=0)
    
    longitude = models.FloatField(default=0)

    mr_latitude = models.FloatField(default=0)
    
    mr_longitude = models.FloatField(default=0)
    
    mr_username = models.CharField(max_length=255)
    
    date = models.DateField()
    time = models.TimeField()
    timestamp = models.CharField(max_length=255, default="00-00-0000")
    ppt_path = models.CharField(max_length=255)

    status = models.CharField(max_length=255, default="pending")

    remark = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.hospital_name
    


#for testing 


class testing(models.Model):

    name = models.CharField(max_length=255)
    rollno = models.IntegerField()


class slide(models.Model):

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    slide_pic = models.ImageField(upload_to="slides" , null=True,  blank=True)


    def __str__(self):
        return self.name



class ppt(models.Model):

    ppt_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    ppt_slides = models.CharField(max_length=255)



    def __str__(self):
        return self.ppt_name


    
    
    
    
    
    
    
    
    
    
    
    
