from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_list', args=[str(self.id)])


class Product(models.Model):
    name = models.TextField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    category = models.ForeignKey("shop.Category", on_delete=models.PROTECT, null=True, related_name='products')
    available = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list', args=[str(self.id)])