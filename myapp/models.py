from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Address=models.CharField(max_length=100,null=True,blank=True)
    Age=models.IntegerField(null=True,blank=True)

class Reg(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Address=models.CharField(max_length=100,null=True,blank=True)

class Studentdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)

class Registerdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Age=models.IntegerField(null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Address=models.CharField(max_length=300,null=True,blank=True)

class Imagedb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="profile",null=True,blank=True)