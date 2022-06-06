# Generated by Django 4.0.4 on 2022-06-06 06:34

import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0019_alter_job_health_insurance_alter_persona_document_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Migration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('passport_id', models.PositiveIntegerField(error_messages={'unique': 'A user with this passport_id ID already exists'}, null=True, unique=True, validators=[django.core.validators.MinValueValidator(10000000, message='Passport ID must contain 8 digits'), django.core.validators.MaxValueValidator(99999999, message='Passport ID must contain 8 digits')])),
            ],
        ),
        migrations.AlterField(
            model_name='persona',
            name='document_id',
            field=models.PositiveIntegerField(error_messages={'unique': 'A user with this document ID already exists'}, null=True, unique=True, validators=[django.core.validators.MinValueValidator(10000000, message='Document ID must contain 8 digits'), django.core.validators.MaxValueValidator(99999999, message='Document ID must contain 8 digits')], verbose_name='Document ID'),
        ),
    ]