# Generated by Django 4.0.5 on 2022-06-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_salary_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeer',
            name='Cuenta_corriente',
            field=models.FloatField(default=0, max_length=50),
        ),
    ]
