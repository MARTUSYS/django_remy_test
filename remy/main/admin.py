from django.contrib import admin
from .models import Catalog, Product
from mptt.admin import DraggableMPTTAdmin


# Отображение каталога
class CatalogAdmin(DraggableMPTTAdmin):
    mptt_indent_field = 'name'
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Catalog, CatalogAdmin)


# Отображение продуктов
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated', 'slug']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', 'price')}


admin.site.register(Product, ProductAdmin)
