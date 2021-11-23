from django.contrib import admin
from .models import Catalog, Product
from mptt.admin import MPTTModelAdmin


admin.site.register(Catalog, MPTTModelAdmin)
admin.site.register(Product)