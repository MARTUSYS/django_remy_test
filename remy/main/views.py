from django.shortcuts import render


def start(request):
    """
    Отображение главной страницы
    :param request:
    :return:
    """
    return render(request, 'main/start.html')


def catalog(request):
    """
    Отображение каталога
    :param request:
    :return:
    """
    return render(request, 'main/catalog.html')
