"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tienda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.catalogo, name='catalogo'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('pedido/', views.crear_pedido, name='crear_pedido_general'),
    path('pedido/<int:producto_id>/', views.crear_pedido, name='crear_pedido'),
    path('seguimiento/', views.seguimiento, name='seguimiento_home'),
    path('seguimiento/<uuid:token>/', views.seguimiento, name='seguimiento_url'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)