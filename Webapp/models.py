from django.db import models


# Create your models here.
class RegisterDB(models.Model):
    User_Name = models.CharField(max_length=100, null=True, blank=True)
    User_Email = models.EmailField(max_length=100, null=True, blank=True)
    User_Password = models.CharField(max_length=100, null=True, blank=True)


class CartDB(models.Model):
    Ct_User = models.CharField(max_length=100, null=True, blank=True)
    Ct_Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Ct_Quantity = models.IntegerField(null=True, blank=True)
    Ct_Total_price = models.IntegerField(null=True, blank=True)
    Ct_Image = models.ImageField(upload_to="Cart Images", null=True, blank=True)


class OrderDB(models.Model):
    Customer_Name = models.CharField(max_length=100, null=True, blank=True)
    Customer_State = models.CharField(max_length=100, null=True, blank=True)
    Customer_Address = models.CharField(max_length=100, null=True, blank=True)
    Customer_City = models.CharField(max_length=100, null=True, blank=True)
    Customer_Mobile = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Customer_Email = models.EmailField(max_length=100, null=True, blank=True)


class ContactDB(models.Model):
    fd_back_Name = models.CharField(max_length=100, null=True, blank=True)
    fd_back_Mobile = models.IntegerField(null=True, blank=True)
    fd_back_Email = models.EmailField(max_length=100, null=True, blank=True)
    fd_back_Subject = models.CharField(max_length=100, null=True, blank=True)
    fd_back_Message = models.CharField(max_length=100, null=True, blank=True)