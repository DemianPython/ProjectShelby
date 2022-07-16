# Generated by Django 4.0.5 on 2022-06-12 06:37

from django.db import migrations, models
import multiprocessing.sharedctypes


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empresa', models.CharField(max_length=100)),
                ('Lista_de_productos', models.CharField(max_length=5000)),
                ('Fecha_de_pedido', models.DateField()),
                ('Fecha_de_entrega', models.DateField(null=multiprocessing.sharedctypes.Value)),
                ('Total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Productos', models.CharField(max_length=3000)),
                ('Debe', models.FloatField()),
                ('Haber', models.FloatField()),
            ],
        ),
    ]
