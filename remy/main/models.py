from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Catalog(MPTTModel):
    """
    иерархическое дерево категорий
    """
    title = models.CharField('Название', max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Родитель", related_name='children')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Product(models.Model):
    """
    Когда вы используете классы FileField или ImageField, Django предоставляет интерфейс программирования приложений
    (API), чтобы открыть вам доступ к файлам. Этот объект – car. photo является файловым объектом, а значит имеет ряд
    атрибутов, описанных ниже.
    """
    title = models.CharField('Название', max_length=255)


class Basket(models.Model):
    """
    корзина \ заказ наборов товаров, изменение статусов заказов, завершение
    """
    ...


class Promo_abstraction(models.Model):
    """
    объединения между собой товаров в “акцию”, с дополнительными условиями
    """
    ...
