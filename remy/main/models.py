from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Catalog(MPTTModel):
    """
    иерархическое дерево категорий
    """
    title = models.CharField('Название', max_length=255, unique=True, db_index=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Родитель",
                            related_name='children')

    def __str__(self):
        return self.title


class Product(models.Model):
    """
    Представление продукта
    """
    category = models.ForeignKey('Catalog', on_delete=models.PROTECT, null=True)

    name = models.CharField('Название', max_length=255, unique=True)
    description = models.TextField('Описание', max_length=512, default='', blank=True)

    image = models.ImageField('Изображение', upload_to='image/%Y/%m/%d', blank=True)

    # Добавить проверку '> 0'
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2)

    stock = models.PositiveIntegerField('На складе', default=1)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    """
    корзина \ заказ наборов товаров, изменение статусов заказов, завершение
    """
    ...


class Promo_abstraction(models.Model):
    """
    объединения между собой товаров в “акцию”, с дополнительными условиями
    """
    ...
