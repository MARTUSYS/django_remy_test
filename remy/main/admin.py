from django.contrib import admin
from .models import Catalog, Product
from mptt.admin import MPTTModelAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated', 'slug']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', 'price', 'stock')}


admin.site.register(Catalog, MPTTModelAdmin)
admin.site.register(Product, CategoryAdmin)
