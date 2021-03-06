from django.shortcuts import render, get_object_or_404
from .models import Product, Catalog
from cart.forms import CartAddProductForm


def start(request):
    """
    Отображение главной страницы
    :param request:
    :return:
    """
    return render(request, 'main/product/start.html')


def product_list(request, category_slug=None):
    """
    Доработать представление класса
    :param category_slug: для отображение товаров экземпляра каталога и его потомков
    :param request:
    :return:
    """
    category = None
    categories = Catalog.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Catalog, slug=category_slug)

        # Показ товаров данной категории и его потомков
        products = products.filter(category__in=category.get_descendants(include_self=True))

        # Для отображения товаров только для выбранной категории
        # products = products.filter(category=category)

    # Применение акции
    for product in products:
        product.price_mod()

    return render(request,
                  'main/product/catalog.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()

    product.price_mod()

    return render(request,
                  'main/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

