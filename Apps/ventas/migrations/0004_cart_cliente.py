# Generated by Django 4.1.1 on 2022-10-28 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('ventas', '0003_alter_venta_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente'),
        ),
    ]
