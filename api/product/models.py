from django.db import models

from api.category.models import Category

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, related_name="products", null=True)
    stock = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to="images/", blank=True, null=True)


    def __str__(self):
        return f"{self.name}"
