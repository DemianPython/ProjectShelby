# Generated by Django 4.0.5 on 2022-06-15 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_salary_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='Empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employeer'),
        ),
    ]
