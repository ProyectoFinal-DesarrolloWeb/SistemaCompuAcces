"""SistemaCompuAcces URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import ProveedorView, ProductosView
from Apps.administracion import views
from .views import CrearProveedorView, CrearProductoView
app_name='administracion'

urlpatterns = [
 path('proveedor/', ProveedorView.as_view(), name='proveedorapp'),
 path('productos/', ProductosView.as_view(), name='productosapp'),


  path('crearProveedor/',CrearProveedorView.as_view(), name='crearproveedor'),
  path('crearProducto/',CrearProductoView.as_view(), name='crearproducto'),
]