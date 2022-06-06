from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .choices import ROL_CHOICES, CIVIL_CHOICES
from django_countries.fields import CountryField

#Snippets

def eigth_digits(field):             #(string)
    validator_eigth=[
            MinValueValidator(10000000, message = field + ' must contain 8 numbers'),
            MaxValueValidator(99999999, message = field + ' must contain 8 numbers')
        ]
    return validator_eigth

def nine_digits(field):              #(string)
    validator_nine=[
            MinValueValidator(100000000, message = field + ' must contain 9 numbers'),
            MaxValueValidator(999999999, message = field + ' must contain 9 numbers')
        ]
    return validator_nine

#Models

class Persona(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    civil_status = models.CharField(
        max_length=8,
        choices= CIVIL_CHOICES,
        default='Single'
    )
    document_id = models.PositiveIntegerField(
        validators=eigth_digits('Document ID'),
        verbose_name='Document ID',
        null=True,
        unique=True,
        error_messages={
            'unique':'A user with this document ID already exists'
        }
    )

    phone_number = models.PositiveIntegerField(
        validators=nine_digits('Phone number'),
        null=True,
    )

    birth_date = models.DateField(auto_now_add=False,auto_now=False,null=True,blank=True)

class Job(models.Model):
    rol = models.CharField(
        max_length=20,
        choices=ROL_CHOICES,
        default='EM'
    )
    health_insurance = models.PositiveIntegerField(
        validators=nine_digits('Health Insurance ID'),
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
        validators=nine_digits('Passport ID'),
        verbose_name='Passport ID',
        null=True,
        unique=True,
        error_messages={
            'unique':'A user with this passport ID already exists'
        }
    )

