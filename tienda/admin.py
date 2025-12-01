from django.contrib import admin
from .models import Insumo, Categoria, Producto, Pedido

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente_nombre', 'estado', 'pago', 'origen', 'fecha_solicitud')
    list_filter = ('estado', 'pago', 'origen')
    search_fields = ('cliente_nombre', 'contacto', 'token')
    readonly_fields = ('token',) # no se toca
    ordering = ('-fecha_solicitud',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio_base', 'destacado')
    list_filter = ('categoria', 'destacado')
    search_fields = ('nombre', 'descripcion')

class InsumoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'cantidad', 'marca', 'color')
    list_filter = ('tipo',)
    search_fields = ('nombre', 'marca')

admin.site.register(Insumo, InsumoAdmin)
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)