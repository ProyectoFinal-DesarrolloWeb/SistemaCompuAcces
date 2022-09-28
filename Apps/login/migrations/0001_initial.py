# Generated by Django 4.1.1 on 2022-09-28 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('nit', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=10)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('telefono', models.CharField(max_length=10)),
                ('usuario', models.CharField(max_length=15)),
                ('contrasenia', models.CharField(max_length=250)),
                ('tipo', models.CharField(choices=[('v', 'Vendedor'), ('a', 'Administrador')], default='v', max_length=1)),
                ('disponibilidad', models.CharField(choices=[('a', 'Activo'), ('i', 'Inactivo')], default='a', max_length=1)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=20)),
                ('icono', models.ImageField(upload_to='')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=45)),
                ('nit', models.CharField(max_length=10)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.cliente')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.empleado')),
                ('producto', models.ManyToManyField(to='login.producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ManyToManyField(to='login.proveedor'),
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.empleado')),
                ('producto', models.ManyToManyField(to='login.producto')),
            ],
        ),
    ]
