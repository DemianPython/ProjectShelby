# Generated by Django 4.0.5 on 2022-06-07 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('SKU', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
