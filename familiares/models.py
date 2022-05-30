from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Persona(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    relationship = models.CharField(max_length=200)

    phone_number = models.PositiveIntegerField(
        validators=[
            MinValueValidator(100000000, message='Telephone number must contain 9 digits'),
            MaxValueValidator(999999999, message='Telephone number must contain 9 digits')
        ]
    )

    birth_date = models.DateField(auto_now_add=False,auto_now=False,null=True,blank=True)
