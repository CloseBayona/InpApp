# Generated by Django 3.2 on 2021-09-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finanzas', '0005_sales_topay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='materials',
            field=models.TextField(blank=True, null=True, verbose_name='Materiales'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='toPay',
            field=models.FloatField(blank=True, null=True, verbose_name='Monto a pagar'),
        ),
    ]
