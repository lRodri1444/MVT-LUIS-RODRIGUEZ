from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .choices import ROL_CHOICES, CIVIL_CHOICES
from django_countries.fields import CountryField

class Persona(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    civil_status = models.CharField(
        max_length=8,
        choices= CIVIL_CHOICES,
        default='Single'
    )
    document_id = models.PositiveIntegerField(
        validators=[
            MinValueValidator(10000000, message='Document ID must contain 8 digits'),
            MaxValueValidator(99999999, message='Document ID must contain 8 digits')
        ],
        verbose_name='Document ID',
        null=True,
        unique=True,
        error_messages={
            'unique':'A user with this document ID already exists'
        }
    )

    phone_number = models.PositiveIntegerField(
        validators=[
            MinValueValidator(100000000, message='Telephone number must contain 9 digits'),
            MaxValueValidator(999999999, message='Telephone number must contain 9 digits')
        ],
        null=True
    )

    birth_date = models.DateField(auto_now_add=False,auto_now=False,null=True,blank=True)

class Job(models.Model):
    rol = models.CharField(
        max_length=20,
        choices=ROL_CHOICES,
        default='EM'
    )
    health_insurance = models.PositiveIntegerField(
        validators=[
            MinValueValidator(100000000, message='Telephone number must contain 9 digits'),
            MaxValueValidator(999999999, message='Telephone number must contain 9 digits')
        ],
        null=True,
        verbose_name= 'Health Insurance ID',
        unique=True,
        error_messages={
            'unique':'A user with this Health Insurance ID already exists'
        }
    )

class Migration(models.Model):
    country = CountryField()
    passport_id = models.PositiveIntegerField(
        validators=[
            MinValueValidator(100000000, message='Passport ID must contain 9 digits'),
            MaxValueValidator(999999999, message='Passport ID must contain 9 digits')
        ],
        verbose_name='Passport ID',
        null=True,
        unique=True,
        error_messages={
            'unique':'A user with this passport_id ID already exists'
        }
    )

