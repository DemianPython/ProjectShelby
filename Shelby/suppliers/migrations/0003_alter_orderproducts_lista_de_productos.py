# Generated by Django 4.0.5 on 2022-06-13 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_alter_orderproducts_fecha_de_entrega_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproducts',
            name='Lista_de_productos',
            field=models.CharField(max_length=10000),
        ),
    ]