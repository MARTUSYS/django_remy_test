from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.start),
    path('catalog', views.product_list, name='product_list'),
    # path('catalog', views.catalog),
]