from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.validators import *


class Thing(AbstractUser):
    name = models.CharField(max_length=30, blank=False)
    quantity = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
            ]
        ,blank=False)
    desc =  models.CharField(max_length=120, blank=True, unique=False)
    


# Create your models here.

