from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator 
from django.core.validators import MaxValueValidator 


class Thing(AbstractUser):
    username = None
    
    name = models.CharField(unique=True,max_length=30, blank=False)
    
    quantity = models.PositiveIntegerField(default=1,blank=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    
    desc =  models.CharField(max_length=120, blank=True)
    
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['name']


# Create your models here.

