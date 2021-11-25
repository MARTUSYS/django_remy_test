from django.shortcuts import render, get_object_or_404
from .models import Product, Catalog


def start(request):
    """
    Отображение главной страницы
    :param request:
    :return:
    """
    return render(request, 'main/product/start.html')


def product_list(request, category_value=None):
    """
    Доработать представление класса
    :param category_value:
    :param request:
    :return:
    """
    category = None
    categories = Catalog.objects.all()  # Настроить развертывание и наследие
    products = Product.objects.filter(available=True)
    if category_value:
        category = get_object_or_404(Catalog, name=category_value)
        products = products.filter(category=category)
    return render(request,
                  'main/product/catalog.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

#
# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     return render(request,
#                   'main/product/detail.html',
#                   {'product': product})
