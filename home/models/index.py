from django.db import models
from .category import Category

class Filter(models.Model):
    img = models.ImageField(upload_to = "upload/filter/")
    name = models.CharField(max_length = 100)

    @staticmethod
    def get_all_filters():
        return Filter.objects.all

class Deals(models.Model):
    img = models.ImageField(upload_to = "upload/dealss/")
    name = models.CharField(max_length = 150)

    @staticmethod
    def get_all_deals():
        return Deals.objects.all

class Ads(models.Model):
    img = models.ImageField(upload_to = "upload/adss/")

    @staticmethod
    def get_all_ads():
        return Ads.objects.all



class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=300, default='', null = True, blank = True)
    image = models.ImageField(upload_to="upload/products/")

    @staticmethod
    def get_all_products():  
        return Product.objects.all

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products() 

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)

    def __str__(self):
        return self.name