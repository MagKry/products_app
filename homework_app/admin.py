from django.contrib import admin

from homework_app.models import Category, Product

# Register your models here.

# admin.site.register(Category) #można to też zamienic na dekorator, jak niżej
# admin.site.register(Product)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    fields = ['category_name']

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

def my_price(obj):
    # return "{:.2f} zł".format(obj.price)
    return f"{obj.price} zł"
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', my_price)
    exclude = ['vat']

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


