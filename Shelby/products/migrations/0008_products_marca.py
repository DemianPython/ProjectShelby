# Generated by Django 4.0.5 on 2022-07-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_quantity_products_cantidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Marca',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
