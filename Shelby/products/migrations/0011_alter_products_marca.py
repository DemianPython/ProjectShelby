# Generated by Django 4.0.5 on 2022-07-16 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0010_alter_suppliers_telefono_de_contacto'),
        ('products', '0010_alter_products_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Marca',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='suppliers.suppliers'),
        ),
    ]
