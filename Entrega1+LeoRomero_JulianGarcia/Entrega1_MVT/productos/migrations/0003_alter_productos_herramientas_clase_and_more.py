# Generated by Django 4.0.4 on 2022-06-08 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_contacto_productos_herramientas_productos_muebles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos_herramientas',
            name='clase',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='productos_herramientas',
            name='energia',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='productos_muebles',
            name='capacidad',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='productos_muebles',
            name='tipo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
