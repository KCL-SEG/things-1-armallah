from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator 
from django.core.validators import MaxValueValidator 


class Thing(models.Model):
    
    name = models.CharField(unique=True,max_length=30, blank=False)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    description =  models.CharField(max_length=120, blank=True)
    


# Create your models here.

