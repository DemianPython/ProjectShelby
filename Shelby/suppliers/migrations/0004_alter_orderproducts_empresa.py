# Generated by Django 4.0.5 on 2022-06-14 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_alter_orderproducts_lista_de_productos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproducts',
            name='Empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.suppliers'),
        ),
    ]