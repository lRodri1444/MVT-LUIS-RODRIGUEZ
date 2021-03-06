# Generated by Django 4.0.4 on 2022-06-05 21:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0010_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='document_id',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(100000000, message='Document ID must contain 8 digits'), django.core.validators.MaxValueValidator(999999999, message='Document ID must contain 8 digits')]),
        ),
    ]
