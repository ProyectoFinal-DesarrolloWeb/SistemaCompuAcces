# Generated by Django 4.1.1 on 2022-10-28 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_cart_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cliente',
        ),
    ]