# Generated by Django 4.1.1 on 2022-10-28 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_cart_cliente'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cotizacion',
        ),
    ]