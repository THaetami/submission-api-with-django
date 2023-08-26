# Generated by Django 4.2.4 on 2023-08-25 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mssalesman', '0005_alter_mssalesmen_sal_bekerjasejak_and_more'),
        ('trpenjualan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trpenjualan',
            name='jul_sal',
            field=models.ForeignKey(db_column='jul_sal_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='penjualan', to='mssalesman.mssalesmen'),
        ),
    ]