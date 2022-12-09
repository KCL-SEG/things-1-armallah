from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator 
from django.core.validators import MaxValueValidator 


class Thing(AbstractUser):
    username = None
    
    name = models.CharField(unique=True,max_length=30, blank=False)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    description =  models.CharField(max_length=120, blank=True)
    
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []


# Create your models here.

