# Generated by Django 4.2.4 on 2023-08-24 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mssalesman', '0002_alter_mssalesmen_sal_aktif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mssalesmen',
            name='sal_aktif',
            field=models.CharField(default='Y', max_length=1),
        ),
    ]
