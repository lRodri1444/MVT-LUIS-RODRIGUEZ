# Generated by Django 4.0.4 on 2022-06-06 11:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0023_alter_migration_passport_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='health_insurance',
            field=models.PositiveIntegerField(error_messages={'unique': 'A user with this Health Insurance ID already exists'}, null=True, unique=True, validators=[django.core.validators.MinValueValidator(100000000, message='Document ID must contain 9 numbers'), django.core.validators.MaxValueValidator(999999999, message='Document ID must contain 9 numbers')], verbose_name='Health Insurance ID'),
        ),
        migrations.AlterField(
            model_name='migration',
            name='passport_id',
            field=models.PositiveIntegerField(error_messages={'unique': 'A user with this passport ID already exists'}, null=True, unique=True, validators=[django.core.validators.MinValueValidator(100000000, message='Document ID must contain 9 numbers'), django.core.validators.MaxValueValidator(999999999, message='Document ID must contain 9 numbers')], verbose_name='Passport ID'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='document_id',
            field=models.PositiveIntegerField(error_messages={'unique': 'A user with this document ID already exists'}, null=True, unique=True, validators=[django.core.validators.MinValueValidator(10000000, message='Document ID must contain 8 numbers'), django.core.validators.MaxValueValidator(99999999, message='Document ID must contain 8 numbers')], verbose_name='Document ID'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='phone_number',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(100000000, message='Document ID must contain 9 numbers'), django.core.validators.MaxValueValidator(999999999, message='Document ID must contain 9 numbers')]),
        ),
    ]
