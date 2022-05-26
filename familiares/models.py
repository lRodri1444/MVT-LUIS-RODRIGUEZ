from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, date

class persona(models.Model):
    name = models.TextField()
    surname = models.TextField()
    relationship = models.TextField()

    phone_number = models.IntegerField(validators=[
        MaxValueValidator(9),
        MinValueValidator(1)
    ],
        blank=True,null=True)

    birth_date = models.DateField(auto_now_add=False,auto_now=False,null=True,blank=True)