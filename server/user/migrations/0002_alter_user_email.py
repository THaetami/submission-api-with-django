# Generated by Django 4.2.4 on 2023-08-24 01:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=225, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
