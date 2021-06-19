from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'menu'

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
		
class Product(models.Model):
    category        = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name     = models.CharField(max_length=45)
    english_name    = models.CharField(max_length=45)
    description     = models.TextField(null=True)
    nutrition       = models.ForeignKey('Nutrition', on_delete=models.SET_NULL, null=True)
    allergies       = models.ManyToManyField('Allergy')

    def __str__(self):
        return self.korean_name

    class Meta:
        db_table = 'products'

class Allergy(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'allergy'

class Image(models.Model):
    image_url   = models.CharField(max_length=2000)
    product     = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2)
    sodium_mg        = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    saturated_fat_g  = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sugars_g         = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    protein_g        = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    caffeine_mg      = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    size_ml          = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'nutritions'
        