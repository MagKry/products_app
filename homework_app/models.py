from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=64, verbose_name='Name')
    slug = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.category_name}"  ' '.join(self.category_name.split("_"))


class Product(models.Model):

    VAT = (
        (1, "0"),
        (2, "0.05"),
        (3, "0.08"),
        (4, "0.23"),
    )

    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.FloatField()
    vat = models.IntegerField(choices=VAT)
    stock = models.IntegerField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        category_names = ', '.join(category.category_name for category in self.categories.all())
        return f"{self.name}"
