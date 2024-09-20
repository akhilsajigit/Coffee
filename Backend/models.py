from django.db import models


class CategoriesDB(models.Model):
    Category_Name = models.CharField(max_length=100, null=True, blank=True)
    Category_Description = models.CharField(max_length=100, null=True, blank=True)
    Category_Image = models.ImageField(upload_to="Category Image", null=True, blank=True)


class ProductsDB(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Product_Price = models.IntegerField(null=True, blank=True)
    Product_Description = models.CharField(max_length=100, null=True, blank=True)
    Product_Image = models.ImageField(upload_to="Product Images", null=True,blank=True)
