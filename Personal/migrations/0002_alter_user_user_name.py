# Generated by Django 3.2 on 2021-06-09 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=150, verbose_name='Nombres del usuario'),
        ),
    ]
