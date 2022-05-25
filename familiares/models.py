from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class persona(models.Model):
    name = models.TextField()
    surname = models.TextField()
    relationship = models.TextField()

    phone_number = models.IntegerField(validators=[
        MaxValueValidator(9),
        MinValueValidator(1)
    ],
        blank=True,null=True)

    birth_date_d = models.IntegerField(validators=[
        MaxValueValidator(2),
        MinValueValidator(1)
    ],
        blank=True,null=True)

    birth_date_m = models.IntegerField(validators=[
        MaxValueValidator(2),
        MinValueValidator(1)
    ],
        blank=True,null=True)

    birth_date_y = models.IntegerField(validators=[
        MaxValueValidator(2),
        MinValueValidator(1)
    ],
        blank=True,null=True)