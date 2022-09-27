# Generated by Django 4.1.1 on 2022-09-27 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_categoria_remove_producto_categoria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=20)),
                ('icono', models.ImageField(upload_to='')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.categoria')),
                ('proveedor', models.ManyToManyField(to='login.proveedor')),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='producto',
            field=models.ManyToManyField(to='login.product'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='producto',
            field=models.ManyToManyField(to='login.product'),
        ),
    ]
