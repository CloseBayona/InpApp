# Generated by Django 3.2 on 2021-09-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finanzas', '0006_auto_20210920_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='company',
            field=models.CharField(max_length=30, verbose_name='Tipo de cliente'),
        ),
    ]
