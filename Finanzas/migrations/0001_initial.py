# Generated by Django 3.2 on 2021-07-05 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.IntegerField(unique=True, verbose_name='Dni/Ruc')),
                ('company', models.BooleanField(default=False, verbose_name='Es una empresa')),
                ('speed', models.CharField(max_length=20, verbose_name='Velocidad de internet')),
                ('province', models.CharField(max_length=50, verbose_name='Provincia a la que pertenece')),
                ('payment', models.CharField(max_length=100, verbose_name='Fecha de pago')),
                ('ip', models.CharField(max_length=300, verbose_name='Cantidad de ip')),
                ('vendor', models.CharField(max_length=150, verbose_name='Vendedor')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre del cliente')),
                ('address', models.CharField(max_length=200, verbose_name='Direccion')),
                ('district', models.CharField(max_length=100, verbose_name='Distrito')),
                ('refference', models.CharField(blank=True, max_length=150, verbose_name='Referencia')),
                ('phone', models.IntegerField(verbose_name='Telefono')),
                ('mail', models.CharField(blank=True, max_length=150, verbose_name='Correo electronico')),
                ('observations', models.TextField(blank=True, verbose_name='Observaciones')),
                ('priority', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1, verbose_name='Prioridad')),
                ('service', models.CharField(choices=[('Tv', 'Tv'), ('Internet', 'Internet'), ('Ambos', 'Ambos')], max_length=10, verbose_name='Servicios')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Fecha')),
                ('install_date', models.DateField(blank=True, verbose_name='Fecha de instalacion')),
                ('materials', models.TextField(blank=True, verbose_name='Materiales')),
                ('price', models.FloatField(verbose_name='Precio')),
            ],
            options={
                'verbose_name': 'Formulario de venta',
                'verbose_name_plural': 'Formularios de ventas',
            },
        ),
    ]
