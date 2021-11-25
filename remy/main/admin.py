from django.contrib import admin
from .models import Catalog, Product
from mptt.admin import DraggableMPTTAdmin

# Отображение каталога
class CatalogAdmin(DraggableMPTTAdmin):
    mptt_indent_field = 'name'


admin.site.register(Catalog, CatalogAdmin)

# Отображение продуктов
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']


admin.site.register(Product, ProductAdmin)
