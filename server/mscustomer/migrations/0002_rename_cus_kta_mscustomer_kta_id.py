# Generated by Django 4.2.4 on 2023-08-24 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mscustomer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mscustomer',
            old_name='cus_kta',
            new_name='kta_id',
        ),
    ]
