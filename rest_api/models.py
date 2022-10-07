from email.policy import default
from itertools import product
from secrets import choice
from django.db import models

class Krosovka(models.Model):
    brand = models.CharField(max_length=100)
    size = models.IntegerField(default=40)
    color = models.CharField(max_length=30)
    price = models.IntegerField(default=40)
    
    def __str__(self):
        return f"{self.brand} brandi"
    
    
    
    
class Mashina(models.Model):
    brand = models.CharField(max_length=100)
    raqami = models.IntegerField(default='555')
    
    def __str__(self):
        return f"{self.brand} brandi"
    
    
    
    
class Mahsulot(models.Model):
    
    SPORT = 'SPORT'
    BAZM = 'BAZM'
    
    PRODUCT_FILTER = (
        (SPORT, 'Sport'),
        (BAZM, 'Bazm')
    )
    brand = models.CharField(max_length=100)
    sifati = models.CharField(max_length=100)
    turi = models.CharField(max_length=6, choices=PRODUCT_FILTER, default=SPORT)
    
    def __str__(self):
        return f"{self.brand} nomli meva"